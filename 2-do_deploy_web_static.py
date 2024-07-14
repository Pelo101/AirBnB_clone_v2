#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""
from fabric.api import run, put, env
import os

env.hosts = ['3.84.237.22', '52.86.145.163']


def do_deploy(archive_path):
    """Function that distributes and archive to web servers"""

    if not os.path.exists(archive_path):
        return False

    archive_file = os.path.basename(archive_path)
    archive_container = archive_file.split('.')[0]
    release_folder = f'/data/web_static/releases/{archive_container}'

    put(archive_path, '/tmp/')
    run(f'mkdir -p {release_folder}')
    run(f'tar -xzvf /tmp/{archive_file} -C {release_folder}')

    run('rm -f /data/web_static/current')
    run(f'ln -s {release_folder} /data/web_static/current')

    return True
