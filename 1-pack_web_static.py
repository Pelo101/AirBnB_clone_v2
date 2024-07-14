#!/usr/bin/python3
""""Module that creates a tgz archive of web_static using fabric"""
import os
import tarfile
from datetime import datetime


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
