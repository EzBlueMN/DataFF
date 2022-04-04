import PySimpleGUI as sg
from constants import *
from functions import *

class MyGraph(sg.Graph):
    def __init__(self):
        super().__init__((GRAPH_SIZE_X, GRAPH_SIZE_Y), (0, GRAPH_SIZE_Y), (GRAPH_SIZE_X, 0),
                          key='-GRAPH-', background_color='#CCCCCC',
                          enable_events=True)


    def draw_dec(self):
        for j in range(0, ALL_ROWS):
            for i in range(0, ALL_COLUMNS):
                char = self.document.get_char(i + j * ALL_COLUMNS)
                char = int2(char, 'ascii')
                x = DEC_CHAR_MARGIN_X + i * DEC_CHAR_SIZE_X + i * DEC_SPACING_X
                y = DEC_CHAR_MARGIN_Y + (j + 1) * DEC_CHAR_SIZE_Y + (j + 1) * DEC_SPACING_Y
                self.draw_text(char, location=(x, y))


    def draw_hex(self):

        # DRAW HEADER
        if draw_header:
            for i in range(0, ALL_COLUMNS):
                char = int2(i, 'hex')
                x = HEX_CHAR_MARGIN_X + i * 2 * HEX_CHAR_SIZE_X + i * HEX_SPACING_X
                y = HEX_CHAR_MARGIN_Y + HEX_SPACING_Y
                self.draw_text(char, location=(x, y), color='blue')
        # DRAW SELECTION
        if self.selection != None:
            if self.new_selection != None:
                i = self.selection[0]
                j = self.selection[1]
                x = HEX_BOX_MARGIN_X + i * HEX_BOX_SIZE_X
                y = HEX_BOX_MARGIN_Y + (j + 1) * HEX_BOX_SIZE_Y
                self.draw_rectangle((x, y), (x + HEX_BOX_SIZE_X, y + HEX_BOX_SIZE_Y), fill_color='#CCCCCC')
                i = self.new_selection[0]
                j = self.new_selection[1]
                self.selection = (i, j)
            else:
                i = self.selection[0]
                j = self.selection[1]
            # DRAW (NEW) SELECTION
            x = HEX_BOX_MARGIN_X + i * HEX_BOX_SIZE_X
            y = HEX_BOX_MARGIN_Y + (j + 1) * HEX_BOX_SIZE_Y
            self.draw_rectangle((x, y), (x + HEX_BOX_SIZE_X, y + HEX_BOX_SIZE_Y), fill_color='white')
        # DRAW VALUES
        for j in range(0, ALL_ROWS):
            for i in range(0, ALL_COLUMNS):
                char = self.document.get_char(i + j * ALL_COLUMNS)
                char = int2(char, 'hex')
                x = HEX_CHAR_MARGIN_X + i * 2 * HEX_CHAR_SIZE_X + i * HEX_SPACING_X
                y = HEX_CHAR_MARGIN_Y + (j + 1) * HEX_CHAR_SIZE_Y + (j + 2) * HEX_SPACING_Y
                self.draw_text(char, location=(x, y))
