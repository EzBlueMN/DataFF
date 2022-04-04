from .DataLines import DataLines
from .AbstractConcept.AbstractConcept import AbstractConcept
from .AbstractConcept.Container import Container
from functions import *

class YAML_FileData(DataLines):
    def __init__(self, lines):
        super().__init__(lines)

    def get_documents(self):
        documents = self.split_in_document('---', first_string_only=True)
        yaml_documents = []
        for document in documents:
            yaml_documents.append(YAML_Document(document))
        return yaml_documents


class YAML_Document(DataLines):
    def __init__(self, lines):
        super().__init__(lines)

    def get_element(self, line) -> tuple:
        depth, cleaned_string = count_depth(line, '  ')
        concept = cleaned_string
        if follow_pattern(string_to_check=cleaned_string, pattern='str:')
        return (depth, concept)

    def create_tree(self):
        root = Container('root')
        for line in self.lines:
            depth, concept = self.get_element(line)

