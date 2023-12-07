#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
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


if __name__ == "__main__":
    # Call the do_pack function when the script is executed
    do_pack()
