class DataLines:
    def __init__(self, lines):
        self.lines = lines
        pass

    def __str__(self) -> str:
        data = ''
        for line in self.lines:
            data += line
        return data

    def merge_lines(self, character:str) -> None:
        new_lines = []
        merge_next_line = False
        for i in range(0, len(self.lines)):
            if len(self.lines[i]) > 1 and self.lines[i][-2] == '\\':
                new_lines.append(self.lines[i][:-2])
            else:
                new_lines.append(self.lines[i])
        self.lines = new_lines

    def split_in_document(self, splitting_line:str, first_string_only=True) -> list:
        documents = []
        line = ''
        document = []
        for i in range(0, len(self.lines)):
            if first_string_only:
                if self.lines[i][:len(splitting_line)] == splitting_line:
                    separator = True
                else:
                    separator = False
            else:
                if self.lines[i] == splitting_line:
                    separator = True
                else:
                    separator = False
            if separator:
                if len(document) > 0:
                    documents.append(document)
                    document = []
            else:
                if len(self.lines) == 0: continue
                # elif self.lines[i][-1:] != '\n': document += self.lines[i]
                # else: document += self.lines[i][:-1]
                elif self.lines[i][-1:] != '\n': document.append(self.lines[i])
                else: document.append(self.lines[i])
        if len(document) > 0:
            documents.append(document)
        return documents


