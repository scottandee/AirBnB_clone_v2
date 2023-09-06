#!/usr/bin/python3
"""This script contains the function do_pack
which generates an archive of the web_static
folder and stores it in the versions folder
"""

from fabric.api import local
from datetime import datetime
import os


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
