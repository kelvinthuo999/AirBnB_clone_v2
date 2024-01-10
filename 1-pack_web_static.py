#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder

    Returns:
        Archive path if successful, None otherwise
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the archive filename
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
        )

        # Create the archive
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path
        return os.path.join("versions", archive_name)

    except Exception as e:
        print(e)
        return None
