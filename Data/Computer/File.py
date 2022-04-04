from .FullPath import FullPath

class File:
    format = 'None'
    def __init__(self):
        self.file_handler = None
        self.full_path = None
        self.path = None
        self.extension = None
        self.mode = None

    def __str__(self) -> str:
        return str(self.full_path)

    def __del__(self):
        return

    def get_path(self):
        return self.full_path

    def set_path(self, full_path):
        self.full_path = FullPath(full_path)
        if self.full_path == None:
            print('WRONG :PPATH')
            return
        self.filename = self.full_path.get_filename()

    def open(self, mode='', full_path=None):
        if full_path != None:
            self.full_path = FullPath(full_path)

        '''
        :param mode:
            r   reading only. The file pointer is placed at the beginning of the file. This is the default mode.
            rb  reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.
            r+  both reading and writing. The file pointer placed at the beginning of the file.
            rb+ both reading and writing in binary format. The file pointer placed at the beginning of the file.
            w   writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
            wb  writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
            w+  writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
            wb+ writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
            a   appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
            ab  appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
            a+  appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
            ab+ appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
        :return:
        '''
        modes = ('r', 'rb', 'r+', 'rb+', 'w', 'wb', 'w+', 'wb+', 'a', 'ab', 'a+', 'ab+')
        self.mode = mode
        if mode not in modes:
            print('WRONG MODE')
            return

        if self.file_handler != None:
            self.file_handler.close()
        self.file_handler = open(str(self.full_path.get_path()), mode)
        if (self.file_handler):
            return True
        return False

    def close(self):
        if self.file_handler:
            self.file_handler.close()
        else:
            print("File can't close an empty file")

    def read(self) -> str:
        if self.can_read():
            return self.file_handler.read()

    def read_lines(self) -> str:
        if self.can_read():
            return self.file_handler.readlines()

    def write(self, data):
        if self.can_write():
            self.file_handler.write(data)

    def can_read(self):
        if 'r' in self.mode:
            return True
        return False

    def can_write(self):
        if 'w' in self.file_handler.mode:
            return True
        return False

    def print(self):
        print(self.path)

    def get_type(self):
        return str(self.data.type)

    def parse(self):
        pass

    def is_valid(self):
        pass

    def get_data(self):
        return self.data.raw
