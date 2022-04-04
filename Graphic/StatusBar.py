import PySimpleGUI as sg
from constants import *

class StatusBar(sg.Text):
    status = sg.Text('', size=(WINDOW_WIDTH, 4), key='-STATUS-')

