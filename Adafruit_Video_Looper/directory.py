# Copyright 2015 Adafruit Industries.
# Author: Tony DiCola
# License: GNU GPLv2, see LICENSE.txt
class DirectoryReader(object):

    def __init__(self, config):
        """Create an instance of a file reader that just reads a single
        directory on disk.
        """
        self._load_config(config)

    def _load_config(self, config):
        self._path = config.get('directory', 'path')

    def search_paths(self):
        """Return a list of paths to search for files."""
        return [self._path]

    def is_changed(self):
        """Return true if the file search paths have changed."""
        # For now just return false and assume the path never changes.  In the
        # future it might be interesting to watch for file changes and return
        # true if new files are added/removed from the directory.  This is 
        # called in a tight loop of the main program so it needs to be fast and
        # not resource intensive.
        return False

    def get_ip():
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255',1))
            IP =  s.getsockname()[0]
        except:
            IP = 'No Network Detected'
        finally:
            s.close()
        return IP

    def idle_message(self):
        """Return a message to display when idle and no files are found."""
        return 'Awaiting Setup - IP: ' + get_ip()


def create_file_reader(config):
    """Create new file reader based on reading a directory on disk."""
    return DirectoryReader(config)
