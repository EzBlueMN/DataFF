import PySimpleGUI as sg

class FileBrowse():
    def __new__(self):
        layout = [sg.InputText(size=(50, 1), key='-FILENAME-', visible=False),
                  sg.FileBrowse(key='-HIDDEN_FILE_BROWSE-', visible=False)]
        return layout
