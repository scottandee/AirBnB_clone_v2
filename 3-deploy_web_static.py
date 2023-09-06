#!/usr/bin/python3
"""This script does a full deploy on my webservers"""

from fabric.api import run, put, env, local
from datetime import datetime
import os


env.user = 'ubuntu'
env.hosts = ['52.91.203.19', '100.25.17.109']


def do_pack():
    """This funcion archives and compresses
    all the contents of the web_static folder
    """
    t = datetime.today()
    arch = f"versions/web_static_{t.year}{t.month}{t.day}\
{t.hour}{t.minute}{t.second}.tgz"

    print(f"Packing web_static to {arch}")

    if not os.path.exists("versions/"):
        local("mkdir versions/")

    result = local(f"tar -cvzf {arch} web_static")
    if result.failed:
        return None
    else:
        arch_size = os.path.getsize(arch)
        print(f"web_static packed: {arch} -> {arch_size}Bytes")
        return arch


def do_deploy(archive_path):
    """This function distributes the archives
    to webservers for testing
    """
    if not os.path.exists(archive_path):
        return False

    path = archive_path.split('/')
    # path = ['versions/', 'web_static_20170315003959.tgz']"

    arch_filename = path[1]
    split_arch = arch_filename.split('.')
    # split_arch = ['web_static_20170315003959', 'tgz']

    server_arch_path = f'/tmp/{arch_filename}'
    xarch_path = f"/data/web_static/releases/{split_arch[0]}"

    if put(archive_path, '/tmp').failed:
        return False

    if run(f"mkdir -p {xarch_path}").failed:
        return False

    if run(f"tar -xzf {server_arch_path} -C {xarch_path}").failed:
        return False

    if run(f"rm {server_arch_path}").failed:
        return False

    if run(f"mv {xarch_path}/web_static/* {xarch_path}").failed:
        return False

    if run(f"rm -rf {xarch_path}/web_static").failed:
        return False

    if run("rm -rf /data/web_static/current").failed:
        return False

    if run(f"ln -s {xarch_path} /data/web_static/current").failed:
        return False

    print("New version deployed!")
    return True


def deploy():
    """This function does full deployment of files to webservers"""

    archive_path = do_pack()
    if archive_path is None:
        return False
    result = do_deploy(archive_path)

    return result
