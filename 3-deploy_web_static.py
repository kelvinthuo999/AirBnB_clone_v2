#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers
"""

from fabric.api import local, env
from os.path import isfile
from datetime import datetime
from fabric.operations import run

env.hosts = ['54.152.236.201', '54.175.134.3']
env.user = 'ubuntu'

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder

    Returns:
        Archive path if successful, None otherwise
    """
    try:
        # Create the "versions" folder if it doesn't exist
        local("mkdir -p versions")

        # Get the current date and time
        now = datetime.now()
        date_time = now.strftime("%Y%m%d%H%M%S")

        # Create the archive path
        archive_path = "versions/web_static_{}.tgz".format(date_time)

        # Compress the contents of the web_static folder into the archive
        local("tar -czvf {} web_static".format(archive_path))

        # Return the archive path if successful
        return archive_path
    except Exception as e:
        # Print an error message and return None if an exception occurs
        print("Error: {}".format(str(e)))
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to your web servers

    Args:
        archive_path (str): Path to the archive to be deployed

    Returns:
        True if all operations have been done correctly, otherwise returns False
    """
    if not isfile(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        run('mkdir -p /tmp/')
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<filename without extension>/
        archive_filename = archive_path.split('/')[-1]
        release_folder = '/data/web_static/releases/{}'.format(archive_filename.split('.')[0])
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Delete the existing symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link to the new version
        run('ln -s {} /data/web_static/current'.format(release_folder))

        print('New version deployed!')
        return True
    except Exception as e:
        print('Error: {}'.format(str(e)))
        return False

def deploy():
    """
    Creates and distributes an archive to your web servers

    Returns:
        True if all operations have been done correctly, otherwise returns False
    """
    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)

if __name__ == "__main__":
    # Example usage: fab -f 3-deploy_web_static.py deploy
    pass
