import PySimpleGUI as sg
from constants import *
from functions import *

class GridGraph(sg.Graph):
    def __init__(self):
        super().__init__((GRAPH_WIDTH, GRAPH_HEIGHT), (0, GRAPH_HEIGHT), (GRAPH_WIDTH, 0),
                          key='-GRID_GRAPH-', background_color=COLOR_GRAPH_BACKGROUND,
                          enable_events=True)

        self.header_offset_grid = self.Grid(left=OFFSET_MARGIN_X, top=MARGIN_Y,
                                     cell_width=OFFSET_CELL_WIDTH, cell_height=OFFSET_CELL_HEIGHT,
                                     text_left=TEXT_MARGIN_X, text_top=TEXT_MARGIN_Y,
                                     columns=1, rows=1,
                                     graph=self)
        self.header_hex_grid = self.Grid(left=HEX_MARGIN_X, top=MARGIN_Y,
                                  cell_width=HEX_CELL_WIDTH, cell_height=HEX_CELL_HEIGHT,
                                  text_left=TEXT_MARGIN_X, text_top=TEXT_MARGIN_Y,
                                  columns=NB_COLUMNS, rows=1,
                                  graph=self)
        self.header_ascii_grid = self.Grid(left=ASCII_MARGIN_X, top=MARGIN_Y,
                                    cell_width=ASCII_CELL_WIDTH, cell_height=ASCII_CELL_HEIGHT,
                                    text_left=TEXT_MARGIN_X, text_top=TEXT_MARGIN_Y,
                                    columns=NB_COLUMNS, rows=1,
                                    graph=self)

        self.offset_grid = self.Grid(left=OFFSET_MARGIN_X, top=OFFSET_MARGIN_Y,
                                     cell_width=OFFSET_CELL_WIDTH, cell_height=OFFSET_CELL_HEIGHT,
                                     text_left=TEXT_MARGIN_X, text_top=TEXT_MARGIN_Y,
                                     columns=1, rows=20,
                                     graph=self)
        self.hex_grid = self.Grid(left=HEX_MARGIN_X, top=HEX_MARGIN_Y,
                                  cell_width=HEX_CELL_WIDTH, cell_height=HEX_CELL_HEIGHT,
                                  text_left=TEXT_MARGIN_X, text_top=TEXT_MARGIN_Y,
                                  columns=NB_COLUMNS, rows=NB_ROWS,
                                  graph=self)
        self.ascii_grid = self.Grid(left=ASCII_MARGIN_X, top=ASCII_MARGIN_Y,
                                    cell_width=ASCII_CELL_WIDTH, cell_height=ASCII_CELL_HEIGHT,
                                    text_left=TEXT_MARGIN_X, text_top=TEXT_MARGIN_Y,
                                    columns=NB_COLUMNS, rows=NB_ROWS,
                                    graph=self)

    class Grid:
        def __init__(self, left, top, cell_width, cell_height, text_left, text_top, columns, rows, graph):
            self.left = left
            self.top = top
            self.cell_width = cell_width
            self.cell_height = cell_height
            self.text_left = text_left
            self.text_top = text_top
            self.columns = columns
            self.rows = rows
            self.graph = graph

        def column_row_from_pos(self, pos):
            if pos < 0:
                return None
            column = pos % self.columns
            row = pos // self.columns
            return (column, row)

        def coord_from_column_row(self, column, row):
            left = self.left + column * self.cell_width
            top = self.top + row * self.cell_height
            right = self.left + (column+1) * self.cell_width
            bottom = self.top + (row+1) * self.cell_height
            return (left, top, right, bottom)

        def column_row_from_x_y(self, x, y):
            if x < self.left: return False
            if x > self.left + self.cell_width * self.columns: return False
            if y < self.top: return False
            if y > self.top + self.cell_height * self.cell_height: return False
            column = (x - self.left) // self.cell_width
            row = (y - self.top) // self.cell_height
            return (column, row)

        def draw_grid(self, size=None, line_color='white', fill_color='white'):
            if size == None:
                for row in range(0,self.rows):
                    for column in range(0, self.columns):
                        self.draw_cell(column, row, line_color=line_color, fill_color=fill_color)
            else:
                for pos in range(0, size):
                    column, row = self.column_row_from_pos(pos)
                    self.draw_cell(column, row, line_color=line_color, fill_color=fill_color)

        def draw_cell(self, column, row, line_color='black', fill_color='white', value=None):
            left, top, right, bottom = self.coord_from_column_row(column, row)
            self.graph.draw_rectangle((left, top), (right, bottom),
                                      fill_color=fill_color,
                                      line_color=line_color, line_width=1)
            if value != None:
                self.write_value(str(value), left, top)

        def erase_cell(self, column, row):
            left, top, right, bottom = self.coord_from_column_row(column, row)
            self.graph.draw_rectangle((left+1, top+1), (right, bottom),
                                      fill_color=COLOR_GRAPH_BACKGROUND,
                                      line_color=COLOR_GRAPH_BACKGROUND)

        def write_value(self, text, left, top):
            self.graph.draw_text(text, location=(left + self.text_left, top + self.text_top))

    def clear(self):
        width, height = self.get_size()
        self.draw_rectangle((0,0), (width, height), fill_color=COLOR_GRAPH_BACKGROUND)

    # def draw_position(self, x, y, box_x, box_y, color):
    #     self.draw_rectangle((x, y), (x+box_x, y+box_y), fill_color=color)

    def load_data(self, data):
        bytes = len(data)
        MAX_HEX_VALUES = NB_ROWS * NB_COLUMNS
        SKIPPED_ROW = 0

        if bytes > MAX_HEX_VALUES:
            size = MAX_HEX_VALUES
        else :
            size = bytes
        self.offset_grid.draw_grid(3, line_color=LINE_COLOR_OFFSET, fill_color=FILL_COLOR_OFFSET)
        self.hex_grid.draw_grid(size, line_color=LINE_COLOR_HEX, fill_color=FILL_COLOR_HEX)
        self.ascii_grid.draw_grid(size, line_color=LINE_COLOR_ASCII, fill_color=FILL_COLOR_ASCII)
        return

        for pos in range(0, size):
            column, row = self.hex_grid.column_row_from_pos(pos)
            left, top, right, bottom = self.hex_grid.coord_from_column_row(column, row)
            self.hex_grid.write_value(int2(data[pos], 'hex'), left, top)

            left, top, right, bottom = self.ascii_grid.coord_from_column_row(column, row)
            self.ascii_grid.write_value(int2(data[pos], 'ascii'), left, top)

        MAX_ASCII_VALUES = NB_ROWS * NB_COLUMNS

    def write_offset_from_position(self, row):
        offset = str(hex(row * NB_COLUMNS)).upper()
        offset = offset[2:]
        offset = offset.zfill(8)
        self.draw_text(offset, location=(x + TEXT_MARGIN_X, y + TEXT_MARGIN_Y), text_location=sg.TEXT_LOCATION_LEFT)

    def write_position(self, char, x, y, color='black'):
        if len(char) > 2: return
        if len(char) == 2: self.draw_text(char, location=(x+10, y+9))
        elif len(char) == 1:
            self.draw_text(char, location=(x+10, y+11))
            self.draw_text('_', location=(x+14, y+11), color='gray')
        else: self.draw_text('__', location=(x + 10, y + 11), color='gray')

    # def draw_static(self):
    #     x = OFFSET_MARGIN_X
    #     y = OFFSET_MARGIN_Y
    #     self.draw_text('Offset', location=(x, y), color='blue')

    def draw_offset(self):
        x = OFFSET_MARGIN_X
        y = OFFSET_MARGIN_Y
        self.draw_text('Offset', location=(x, y), color='blue')
        for j in range(0, NB_ROWS):
            offset = j * NB_COLUMNS
            x = OFFSET_MARGIN_X
            y = OFFSET_MARGIN_Y + (j + 1) * OFFSET_CHAR_Y
            self.draw_text(offset, location=(x, y))


    def draw_dec(self):
        for j in range(0, NB_ROWS):
            for i in range(0, NB_COLUMNS):
                char = self.document.get_char(i + j * NB_COLUMNS)
                char = int2(char, 'ascii')
                x = ASCII_MARGIN_X + i * ASCII_WIDTH + i * ASCII_SPACING_X
                y = ASCII_MARGIN_Y + (j + 1) * ASCII_HEIGHT + (j + 1) * ASCII_SPACING_Y
                self.draw_text(char, location=(x, y))


    def draw_hex(self):
        draw_boxes = True
        draw_header = True
        # DRAW BOXES
        if draw_boxes:
            x = HEX_MARGIN_X
            y = HEX_MARGIN_Y
            width = NB_COLUMNS * HEX_WIDTH + 1
            height = (NB_ROWS + 1) * HEX_HEIGHT
            for i in range(0, NB_COLUMNS + 1):
                self.draw_line((x + i * HEX_WIDTH, y), (x + i * HEX_WIDTH, y + height))
            for j in range(0, NB_ROWS + 2):
                self.draw_line((x, y + j * HEX_HEIGHT), (x + width, y + j * HEX_HEIGHT))
        # DRAW HEADER
        if draw_header:
            for i in range(0, NB_COLUMNS):
                char = int2(i, 'hex')
                x = HEX_CHAR_MARGIN_X + i * 2 * HEX_CHAR_SIZE_X + i * HEX_SPACING_X
                y = HEX_CHAR_MARGIN_Y + HEX_SPACING_Y
                self.draw_text(char, location=(x, y), color='blue')
        # DRAW SELECTION
        if self.selection != None:
            if self.new_selection != None:
                i = self.selection[0]
                j = self.selection[1]
                x = HEX_MARGIN_X + i * HEX_WIDTH
                y = HEX_MARGIN_Y + (j + 1) * HEX_HEIGHT
                self.draw_rectangle((x, y), (x + HEX_WIDTH, y + HEX_HEIGHT), fill_color='#CCCCCC')
                i = self.new_selection[0]
                j = self.new_selection[1]
                self.selection = (i, j)
            else:
                i = self.selection[0]
                j = self.selection[1]
            # DRAW (NEW) SELECTION
            x = HEX_MARGIN_X + i * HEX_WIDTH
            y = HEX_MARGIN_Y + (j + 1) * HEX_HEIGHT
            self.draw_rectangle((x, y), (x + HEX_WIDTH, y + HEX_HEIGHT), fill_color='white')
        # DRAW VALUES
        for j in range(0, NB_ROWS):
            for i in range(0, NB_COLUMNS):
                char = self.document.get_char(i + j * NB_COLUMNS)
                char = int2(char, 'hex')
                x = HEX_CHAR_MARGIN_X + i * 2 * HEX_CHAR_SIZE_X + i * HEX_SPACING_X
                y = HEX_CHAR_MARGIN_Y + (j + 1) * HEX_CHAR_SIZE_Y + (j + 2) * HEX_SPACING_Y
                self.draw_text(char, location=(x, y))