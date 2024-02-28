#!/usr/bin/python3
"""
Generate .tgz files and deploys it to
web servers
"""

from time import strftime
from fabric.api import env, run, put, local
import os

env.hosts = ['54.157.134.178', '54.175.136.136']
env.user = "ubuntu"


def do_pack():
    """Generate a .tgz file of web_static folder"""
    try:
        # create versions folder
        local("mkdir -p versions")
        # compress to versions folder
        time = f"{strftime('%Y%M%d%H%M%S')}"
        local(f"tar -cvzf versions/web_static_{time}.tgz web_static/")
        # return filename
        return f'verizon/web_static_{time}.tgz'
    except Exception:
        return None


def do_deploy(archive_path):
    """
    Deploys archive to both servers
    """
    if os.path.exists(archive_path):
        filetag = archive_path.split("/")[-1]
        tag = filetag.split(".")[0]
        new_path = f"/data/web_static/releases/{tag}/"
        sym_link = "/data/web_static/current"
        # upload file to /tmp/
        put(archive_path, f"/tmp/{filetag}")
        # create target directory
        run(f"sudo mkdir -p {new_path}")
        # uncompress folders to target_directory
        run(f"sudo tar -xzf /tmp/{filetag} -C {new_path}")
        # delete archive
        run(f"sudo rm /tmp/{filetag}")
        # move files from web_static to root of target folder
        run(f"sudo mv {new_path}web_static/* {new_path}")
        # delete empty web_static directory
        run(f"sudo rm -rf {new_path}web_static")
        # delete sym link /data/web_static/current
        run(f"sudo rm -rf {sym_link}")
        # create new sym link
        run(f"sudo ln -s {new_path} {sym_link}")
        print("New version deployed!")
        return True
    return False
