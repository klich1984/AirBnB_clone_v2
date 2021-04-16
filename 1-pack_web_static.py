#!/usr/bin/python3
"""  script that generates a .tgz archive """
from fabric.api import local
import datetime
from os.path import getsize


def do_pack():
    """generates a .tgz archive from the contents of the web_static
    folder of your AirBnB"""
    local('mkdir -p versions')
    dt = datetime.datetime.now()
    dt = dt.strftime('%Y%m%d%H%M%S')
    path = './versions/web_static_{}.tgz'.format(dt)
    try:
        local("tar -cvzf ./versions/web_static_{}.tgz web_static".format(dt))
        # sz = getsize(path)
        print('web_static packed: versions/web_static_20170314233357.tgz\
              -> {}Bytes'.format(getsize(path)))
    except Exception:
        return None
