from lmnopy import

from constants import *

def my_app():
    from Logic.Logic import Logic
    from Changes.Observer import Observer
    logic = Logic()
    observer = Observer(logic)
    observer.start()

def test_file():
    from Data.Computer.File import File
    from Data.Computer.FullPath import FullPath
    from Data.DataLines import DataLines
    from Data.YAML_Data import YAML_FileData
    from Data.YAML_Data import YAML_Document

    full_path = FullPath(YAML_FILE_FORMAT_PATH + 'test.yaml')
    if full_path:
        file = File()
        file.open(mode='r', full_path=full_path)
        yaml_file = YAML_FileData(file.read_lines())
        yaml_documents = yaml_file.get_documents()
        for yaml_document in yaml_documents:
            yaml_document.create_tree()


def tree():
    from Data.AbstractConcept.Container import Container
    from Data.AbstractConcept.Content import Content

    root = Container('root')

    bonjour = Content('bonjour')
    final = Content('final')

    branch1 = Container('branch1')
    branch1.add(bonjour)

    branch2 = Container('branch2')
    branch2.add(final)

    root.add(branch1)
    root.add(branch2)

    root.print_tree()

def reg_ex():
    from Data.Pattern.Pattern import Pattern
    p = Pattern()
    p.test()

if __name__ == '__main__':
    reg_ex()
    # test_file()
    # my_app()
