#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import local, env, put, run
from datetime import datetime
import os
import os.path as path

env.hosts = ['35.237.246.228', '35.190.168.95']
now = datetime.now()
dt_string = now.strftime("%Y%m%d%H%M%S")


def do_pack():
    """script that generates a .tgz archive"""
    try:
        local('mkdir -p versions/')
        filename = "web_static_" + dt_string + ".tgz"
        local('tar -cvzf versions/{} web_static/'.format(filename))
        path = 'versions/{}'.format(filename)
        print("web_static packed: {} ->{}Bytes"
              .format(path, os.path.getsize(path)))
        return path
    except:
        return None


def do_deploy(archive_path):
    """function2"""
    token_path = archive_path.split("/")
    path1 = token_path[1]
    token_path2 = token_path[1].split(".")
    path2 = token_path2[0]

    if path.exists(archive_path):
        put(archive_path, "/tmp/")
        run("sudo mkdir -p  /data/web_static/releases/{}/".format(path2))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(path1, path2))
        run("sudo rm /tmp/{}".format(path1))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/".format(path2, path2))
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(path2))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} \
/data/web_static/current".format(path2))
        return True
    else:
        return False


def deploy():
    """ Function task 3 """
    variable = do_pack()
    if path.exists(variable):
        return do_deploy(variable)
    else:
        return False
