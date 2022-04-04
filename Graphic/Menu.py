import PySimpleGUI as sg

# Use Alf+F to navigate Menu with the shortcut defined with & before the letter
# Use 'Text to show::KeyForItem'

class Menu(sg.Menu):
    def __init__(self):
        menu_def = [['&File', ['&Open a file  Ctrl-O::test',
                               '&Save         Ctrl-S',
                               '&Save as',
                               '&Properties',
                               'E&xit         Alt+F4']],
                    ['&Edit', ['&Paste',['Special',
                                         'Normal', ],
                               'Undo'],
                     ],
                    ['&Toolbar', ['---', 'Command &1', 'Command &2',
                                  '---', 'Command &3', 'Command &4']],
                    ['&Help', '&About...'], ]
        super().__init__(menu_def, tearoff=False, pad=(200, 1))