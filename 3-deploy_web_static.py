#!/usr/bin/python3
""""Module that deploys an archive"""
import os
import tarfile
from datetime import datetime
from fabric.api import run, put, env


env.hosts = ['3.84.237.22', '52.86.145.163']


def do_pack():
    """A function that creates a tgz archive"""

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"

    if not os.path.exists("versions"):
        os.makedirs("versions")

    if os.path.exists("web_static"):
        with tarfile.open(archive_name, "w:gz") as tar:
            tar.add("web_static", arcname=os.path.basename("web_static"))

        if os.path.exists(archive_name):
            return archive_name

    return None


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


def deploy():
    """Deploy function to create and distributive archive"""

    archive_path = do_pack()
    if not archive_path:
        return False
    deploy_result = do_deploy(archive_path)
    return deploy_result
