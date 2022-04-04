import PySimpleGUI as sg
from constants import *
from functions import *

class MyMenu(sg.Menu):
    def __init__(self):
        menu_def = [['&File', ['&Open     Ctrl-O', '&Save       Ctrl-S', '&Properties', 'E&xit']],
                    ['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo'], ],
                    ['&Toolbar', ['---', 'Command &1', 'Command &2',
                                  '---', 'Command &3', 'Command &4']],
                    ['&Help', '&About...'], ]
        super().__init__(menu_def, tearoff=False, pad=(200, 1))
