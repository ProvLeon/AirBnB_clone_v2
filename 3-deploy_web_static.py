#!/usr/bin/python3
# Creates and distributes an archive to my web servers using deploy.
import os.path
from datetime import datetime
from fabric.api import env, put, run, local

env.hosts = ['18.207.233.152', '100.26.221.176']


def do_pack():
    """
    Create a .tgz archive from web_static content.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{timestamp}.tgz"

    if not os.path.exists("versions"):
        os.makedirs("versions")

    result = local(f"tar -czvf {archive_path} web_static")
    return archive_path if result.succeeded else None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers and deploys it
    """

    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, f"/tmp/{file}").failed is True:
        return False
    if run(f"rm -rf /data/web_static/releases/{name}/").failed is True:
        return False
    if run(f"mkdir -p /data/web_static/releases/{name}/").failed is True:
        return False
    if (
        run(
            f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}/"
        ).failed
        is True
    ):
        return False
    if run(f"rm /tmp/{file}").failed is True:
        return False
    if (
        run(
            f"mv /data/web_static/releases/{name}/web_static/* \
                    /data/web_static/releases/{name}/"
        ).failed
        is True
    ):
        return False
    if (
        run(f"rm -rf /data/web_static/releases/{name}/web_static").failed
        is True
    ):
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    return (
        run(
            f"ln -s /data/web_static/releases/{name}/ /data/web_static/current"
        ).failed
        is not True
    )


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    return False if file is None else do_deploy(file)
