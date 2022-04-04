class FullPath:
    def __init__(self, full_path):
        if isinstance(full_path, FullPath):
            self.full_path = full_path.get_path()
        else:
            self.full_path = full_path

    def __str__(self):
        return self.full_path

    def valid(self):
        return True

    def get_path(self):
        return self.full_path.__str__()

    def set_path(self, full_path):
        self.full_path = full_path

    def get_extension(self):
        sections = self.full_path.split('.')
        if len(sections) == 1:  # No extension
            return ''
        else:
            return sections[len(sections) - 1]

    def get_filename(self):
        return "TODO"

    def get_folder(self):
        return "TODO"