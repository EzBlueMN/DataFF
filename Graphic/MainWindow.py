import PySimpleGUI as sg
from .FileBrowse import FileBrowse
from .GridGraph import GridGraph
from .LogicTree import LogicTree
from .Menu import Menu
from .StatusBar import StatusBar
from .ToolBar import ToolBar
from constants import *
from functions import *

class MainWindow(sg.Window):
    def __init__(self):
        ### LAYOUTS DEFINITIONS
        self.menu = Menu()
        self.toolbar = ToolBar()
        self.tree = LogicTree()
        self.graph = GridGraph()
        self.status = StatusBar()
        self.file_browse = FileBrowse()
        self.column = sg.Column([[self.graph]],
                                size=(COLUMN_WIDTH, COLUMN_HEIGHT),
                                background_color=COLUMN_BACKGROUND_COLOR,
                                scrollable=True, vertical_scroll_only=True)

        self.layout = [[self.menu],
                       [self.toolbar],
                       [self.tree, self.column],
                       [self.status],
                       self.file_browse]

        ### WINDOW DEFINITION
        super().__init__('File Format', self.layout,
                         size=(WINDOW_WIDTH, WINDOW_HEIGHT), location=(0, 0),
                         margins=(0, 0), resizable=False,
                         return_keyboard_events=True,
                         font=WINDOW_FONT, finalize=True)

        self.maximize()

        # DIFFERENT ALLOCATIONS
        self.focus = None
        self.selection = None
        self.new_selection = None

    def set_status(self, status):
        self.status.update(status)

    def open_file(self):
        self.graph.clear()
        self['-HIDDEN_FILE_BROWSE-'].click()
        full_path = self['-FILENAME-'].get()
        self.status.update(full_path)
        return full_path

    def create_grid(self, size):
        import math

        self.graph.header_offset_grid.draw_grid()
        self.graph.header_hex_grid.draw_grid()
        self.graph.header_ascii_grid.draw_grid()

        self.graph.offset_grid.draw_grid(math.ceil(size/NB_COLUMNS))
        self.graph.hex_grid.draw_grid(size)
        self.graph.ascii_grid.draw_grid(size)

    def set_size(self, size):
        if size > max_size: size = max_size

        left = HEX_MARGIN_X
        up = HEX_MARGIN_Y + HEX_SPACING_Y
        box_x = HEX_CHAR_WIDTH * 2 + HEX_SPACING_X
        box_y = CHAR_HEIGHT
        columns = NB_COLUMNS
        rows = NB_ROWS

        # # MAKE "Offset boxes"
        # for pos in range(1, 30):
        #     x, y = pos_to_coord(pos, left=OFFSET_MARGIN_X, up=OFFSET_MARGIN_Y,
        #                         box_x=OFFSET_WIDTH, box_y=CHAR_HEIGHT, columns=1, rows=NB_ROWS)
        #     self.draw_position(x, y, box_x=OFFSET_WIDTH, box_y=CHAR_HEIGHT, color='green')


        for pos in range(16, size):
            x, y = pos_to_coord(pos, left, up, box_x, box_y, columns, rows)
            self.graph.draw_position(x, y, box_x, box_y, 'white')
            self.graph.write_position('FF', x, y)

    def update_tree(self, data):
        tree_data = sg.TreeData()
        for d in data:
            tree_data.Insert(d[0], d[1], d[2], d[3])
            self.tree.update(tree_data)

    def click(self, x, y, graph):
        values = self.graph.hex_grid.column_row_from_x_y(x, y)
        if values:
            column, row = values
            self.graph.hex_grid.draw_cell(column, row, line_color='yellow', fill_color='blue', value='00')

    def update_menu(self):
        new_def = [['&File', ['&Open a file  Ctrl-O::test',
                              '&Save         Ctrl-S',
                              '&Save as',
                              '&Properties',
                              'E&xit         Alt+F4']]]
        self.menu.update(new_def)

    def drag(self, x, y, graph):
        self['-GRID_GRAPH-'].draw_point((x, y), color='blue', size=20)

    def move(self, x, y, graph):
        self['-GRID_GRAPH-'].draw_point((x, y), color='red')