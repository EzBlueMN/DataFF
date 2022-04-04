from Data.Computer.File import File
from Data.Computer.FullPath import FullPath
from Graphic.MainWindow import MainWindow


class Logic:
    def __init__(self):
        self.main = MainWindow()
        self.file = None
        self.main.set_status('None')

        self.modify_start()

    def update_status(self, text):
        self.main.set_status(text)

    def modify_start(self):
        self.main.update_menu()
        self.update_tree()
        full_path = FullPath('D:\Python\Projets\All_FileFormat\constants.py')
        self.file = File()
        self.file.open('rb+', full_path)
        data = self.file.read()
        self.main.graph.load_data(data)

    def open_file(self):
        full_path_from_window = self.main.open_file()
        if full_path_from_window == '': return
        full_path = FullPath(full_path_from_window)
        if full_path.valid() == False:
            print('WRONG PATH')
        self.file = File()
        self.file.open('rb+', full_path)
        data = self.file.read()
        self.main.graph.load_data(data)

    # def highlight_pos(self, first, last, self.file.data):
    #     self.main.hex_grid.draw()

    def update_tree(self):
        data = []
        data.append(('', '-ROOT-', 'This is the root', [0, 4]))
        data.append(('-ROOT-', '-E1-', 'This is E1 in root', [0, 4]))
        data.append(('-ROOT-', '-E2-', 'This is E2 in root', [0, 2]))
        self.main.update_tree(data)

    def read(self):
        return self.main.read()

    def close(self):
        self.main.close()

    def mouse_move(self, x, y, graph):
        self.main.move(x, y, graph)

    def mouse_drag(self, x, y, graph):
        self.main.drag(x, y, graph)

    def mouse_click(self, x, y, graph):
        self.main.click(x, y, graph)
