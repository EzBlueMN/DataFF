import PySimpleGUI as sg
from functions import *
from Data.Document import Document
from .MyGraph import MyGraph
from .MyMenu import MyMenu
from .MyTree import MyTree

class FileFormatGUI:
    def __init__(self):
        ### LAYOUTS DEFINITIONS
        menu = MyMenu()
        tree = MyTree()
        graph = MyGraph()

        column = sg.Column([[graph]], size=(COLUMN_SIZE_X, COLUMN_SIZE_Y),
                           background_color=COLUMN_BACKGROUND_COLOR,
                           scrollable=True, vertical_scroll_only=True)

        event = sg.Text('', size=(WINDOW_SIZE_X, 1), key='-EVENTS-')
        status = sg.Text('', size=(WINDOW_SIZE_X, 4), key='-STATUS-')

        # self.layout = [[[menu], tree, offset, hex, dec],[event],[status]]
        self.layout = [[[menu], tree, column], [event], [status]]

        ### WINDOW DEFINITION
        self.window = sg.Window('File Format', self.layout,
                                size=(WINDOW_SIZE_X, WINDOW_SIZE_Y), location=(0,0),
                                margins=(0,0), resizable=False,
                                return_keyboard_events=True,
                                font=WINDOW_FONT, finalize=True)
        self.window.Maximize()

        graph.draw_offset()
        graph.draw_dec()
        graph.draw_hex()

        # DIFFERENT ALLOCATIONS
        self.document = Document()
        self.focus = None
        self.selection = None
        self.new_selection = None

    def find_dec_click(self):
        pass

    def find_hex_click(self):
        pass

    def write_events(self):
        events = self.window['-EVENTS-']
        events.update(self.event + str(self.values))

    def write_status(self, status, key=False):
        text = self.window['-STATUS-']
        if key:
            text.update(status)
            return
        if status not in ('-OFFSET-', '-DEC-', '-HEX-', '-TREE-'):
            text.update('Wrong window got focus:' + status)
            return
        text.update('Focus to ' + status)

    def run(self):
        while True:
            self.event, self.values = self.window.read()
            if self.event in (sg.WIN_CLOSED, 'Exit'):
                break
            self.write_events()
            if self.event == '-ADRESS-':
                self.write_status('-ADRESS-')
            elif self.event == '-DEC-':
                self.write_status('-DEC-')
            elif self.event == '-HEX-':
                click = self.values['-HEX-']
                self.selection = (2, 3)
                self.draw_hex()
                self.write_status('-HEX-')
            elif self.event == '-TREE-':
                self.write_status('-TREE-')
            if self.event is not sg.TIMEOUT_KEY:
                key = self.event
                if key in ('Escape:27'):
                    break
                if key in ('Left:37', 'Up:38', 'Right:39', 'Down:40') and self.selection != None:
                    if key == 'Left:37':
                        if self.selection[0] != 0:
                            self.new_selection = (self.selection[0]-1, self.selection[1])
                    elif key == 'Up:38':
                        if self.selection[1] != 0:
                            self.new_selection = (self.selection[0], self.selection[1]-1)
                    elif key == 'Right:39':
                        if self.selection[0] < ALL_COLUMNS:
                            self.new_selection = (self.selection[0]+1, self.selection[1])
                    else: # Down
                        if self.selection[1] < ALL_ROWS:
                            self.new_selection = (self.selection[0], self.selection[1]+1)
                    self.draw_hex()
                if len(self.event) == 1:
                    message = '{} - {}'.format(key, ord(key))
                    self.write_status(message, True)
                else:
                    self.write_status(key, True)

        self.window.close()