from os import path
from FileExplorer.File import File
from .FullPath import Path

class Folder:
    def __init__(self):
        self.path = None
        self.folders = []
        self.files = []

    def setPath(self, path):
        if isinstance(path, Path):
            self.path = path
        else:
            self.path = Path()
            self.path.setPath(path)

    def __str__(self):
        return str(self.path)

    def __contains__(self, filename):
        return path.exists(self.path + filename)

    def __iadd__(self, object):
        if isinstance(object, File):
            self.files.append(object)
        elif isinstance(object, Folder):
            self.folders.append(object)
        else:
            print('wrong type', type(object))
        return self

    def print(self):
        print(self.path)
        if len(self.files) != 0:
            print('files')
        for file in self.files:
            file.print()
        if len(self.folders) != 0:
            print('folders')
        for folder in self.folders:
            print(folder)
