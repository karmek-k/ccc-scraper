import os

from downloader import constants
from downloader.errors import ResourceNotFoundError


ROOT_DIR = constants.RESOURCE_ROOT_DIR


def _none_to_empty(string=None):
    """Returns an empty string if `string is None`, else returns the string unchanged"""

    return '' if string is None else string


class Resource:
    def __init__(self, name, subdirectory=None, content=None):
        self.name = name
        self.subdirectory = subdirectory
        self.content = content


    @staticmethod
    def make_path(name=None, subdirectory=None):
        """Builds the path to a resource or a subdirectory"""

        # make sure it ends with a slash
        root = ROOT_DIR if ROOT_DIR[-1] == '/' else f'{ROOT_DIR}/'

        # `None` to empty string
        name = _none_to_empty(name)
        subdirectory = _none_to_empty(subdirectory)

        return os.path.join(root, subdirectory, name)


    def _make_path(self):
        """Private version of make_path"""

        return Resource.make_path(self.name, self.subdirectory)


    def is_saved(self):
        """Is the resource saved on disk"""

        maybe_path = self._make_path()

        return os.path.isfile(maybe_path)


    def get_path(self):
        """Returns the path of a resource, or `None` if there is no such resource"""

        maybe_path = self._make_path()

        if self.is_saved():
            return maybe_path
        return None


    def read(self):
        """Gets a resource's text content. Raises `ResourceNotFoundError` if not found"""

        path = self.get_path()

        if path is None:
            raise ResourceNotFoundError(self)
        with self.open() as f:
            return f.read()


    def save(self):
        """Adds a new resource file. Creates the resource directory if it does not exist"""

        path = self.get_path()
        directory, _ = os.path.split(path)

        if not os.path.exists(directory):
            os.mkdir(directory)

        with self.open('w') as f:
            f.write(self.content)


    def open(self, mode='r', encoding='UTF-8'):
        """
        Opens a resource file using the `open()` function.
        Raises a `FileNotFoundError` if the resource could not be found
        """

        path = self.get_path()
        if path is None:
            raise FileNotFoundError(f'Did not find file: {self._make_path()}')
        return open(path, mode, encoding=encoding)


    def list_resources(self, subdirectory=None):
        """
        Returns an iterable object of resources in the root directory.
        If `subdirectory` is given, then lists resources only in that subdirectory.
        """

        subdirectory_path = Resource.make_path(subdirectory=subdirectory)

        return filter(self.is_saved, os.listdir(subdirectory_path))
        