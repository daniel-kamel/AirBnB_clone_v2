#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static"
              .format(datetime.now().strftime("%Y%m%d%H%M%S")))
        return "versions/web_static_{}.tgz".format(datetime.now().strftime("%Y%m%d%H%M%S"))
    except:
        return None
