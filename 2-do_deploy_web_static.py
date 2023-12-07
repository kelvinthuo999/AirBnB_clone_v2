#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from fabric.api import put, run, env
from os.path import exists


env.hosts = ['54.152.236.201', '54.175.134.3']
env.user = 'ubuntu' 


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers

    Args:
        archive_path (str): Path to the archive to be deployed

    Returns:
        True if all operations have been done correctly, otherwise returns False
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
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


if __name__ == "__main__":
    # Example usage: fab -f 2-do_deploy_web_static.py do_deploy:<path_to_archive>
    pass
