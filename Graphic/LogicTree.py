import PySimpleGUI as sg
from constants import *

class LogicTree(sg.Tree):
    def __init__(self):
        tree_data = sg.TreeData()

        super().__init__(data=tree_data,
                         headings=['Size', 'Range'],
                         auto_size_columns=True,
                         select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
                         num_rows=TREE_NB_ROWS,
                         font=TREE_FONT,
                         col0_width=TREE_FIRST_WIDTH,
                         def_col_width=TREE_DEFAULT_WIDTH,
                         key='-TREE-',
                         show_expanded=False,
                         enable_events=True,
                         expand_x=True,
                         expand_y=True)