#!/usr/bin/python3
"""Generates a .tgz archive from the contents
of the web_static folder.
"""

from fabric.api import task, local
from datetime import datetime
import os


@task
def do_pack():
    '''
    This function compresses the web_static directory
    '''

    date_obj = datetime.now()
    year = date_obj.year
    month = date_obj.strftime('%m')
    day = date_obj.strftime('%d')
    hour = date_obj.strftime('%H')
    minute = date_obj.strftime('%M')
    second = date_obj.strftime('%S')

    path = f'versions/web_static_{year}{month}{day}{hour}{minute}{second}.tgz'

    if not os.path.exists('versions'):
        os.makedirs('versions')

    result = local(f'tar -czvf {path} web_static', capture=True)

    if result.succeeded:
        return path
    else:
        return None
