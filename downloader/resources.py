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


    @staticmethod
    def is_saved(name, subdirectory=None):
        """Is the resource saved on disk"""

        maybe_path = Resource.make_path(name, subdirectory)

        return os.path.isfile(maybe_path)


    @staticmethod
    def get_path(name=None, subdirectory=None):
        """Returns the path of a resource, or `None` if there is no such resource"""

        maybe_path = Resource.make_path(name, subdirectory)

        if Resource.is_saved(name, subdirectory):
            return maybe_path
        return None
    

    def _get_path(self):
        """Private version of get_path"""

        return Resource.get_path(self.name, self.subdirectory)


    def read(self):
        """Gets a resource's text content. Raises `ResourceNotFoundError` if not found"""

        path = self._get_path()

        if path is None:
            raise ResourceNotFoundError(self)
        with self.open() as f:
            return f.read()


    def save(self):
        """Adds a new resource file. Creates the resource directory if it does not exist"""

        directory = ROOT_DIR

        if self.subdirectory is not None:
            directory = os.path.join(directory, self.subdirectory)

        if not os.path.exists(directory):
            os.mkdir(directory)

        with self.open('w') as f:
            f.write(self.content)


    def open(self, mode='r', encoding='UTF-8'):
        """
        Opens a resource file using the `open()` function.
        """

        path = self._make_path()
        return open(path, mode, encoding=encoding)


    @classmethod
    def list_resources(cls, subdirectory=None):
        """
        Returns an iterable object of resources in the root directory.
        If `subdirectory` is given, then lists resources only in that subdirectory.
        """

        subdirectory_path = cls.make_path(subdirectory=subdirectory)

        for name in os.listdir(subdirectory_path):
            if cls.is_saved(name, subdirectory):
                yield cls(name, subdirectory)


    def __str__(self):
        return self._make_path()


    def __repr__(self):
        return f'<Resource: {self.__str__()}>'
