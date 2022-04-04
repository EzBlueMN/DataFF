import PySimpleGUI as sg
from constants import *
from functions import *

class MyTree(sg.Tree):
    def __init__(self):
        tree_data = sg.TreeData()
        tree_data.Insert('', '-ROOT-', 'This is the root', [0, 0])
        tree_data.Insert('-ROOT-', '-E1-', 'This is E1 in root', [0, 0])
        tree_data.Insert('-ROOT-', '-E2-', 'This is E2 in root', [0, 0])

        super().__init__(data=tree_data,
                         headings=['Size', 'Range'],
                         auto_size_columns=True,
                         select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
                         num_rows=TREE_ROWS,
                         font=TREE_FONT,
                         col0_width=TREE_FIRST_WIDTH,
                         def_col_width=TREE_DEFAULT_WIDTH,
                         key='-TREE-',
                         show_expanded=False,
                         enable_events=True,
                         expand_x=True,
                         expand_y=True)


