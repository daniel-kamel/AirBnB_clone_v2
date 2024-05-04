#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""
from fabric.api import put, run, env
from datetime import datetime
import os

env.user = "ubuntu"
env.hosts = ["35.174.204.185", "54.237.8.132"]


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        path = "/data/web_static/releases/{}/".format(no_ext)
        run("mkdir -p {}".format(path))
        run("tar -xzf {} -C {}".format(archive_path, path))
        run("rm {}".format(archive_path))
        run("mv {}/web_static/* {}".format(path, path))
        run("rm -rf {}/web_static".format(path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path))
        return True
    except Exception:
        return False
