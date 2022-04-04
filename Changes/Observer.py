from .Input import *

class Observer:
    def __init__(self, logic):
        self.logic = logic

    def start(self):
        # Give the Model to all commands
        Input.logic = self.logic
        do_mouse = True
        do_keyboard = False
        print_all_events = True
        while True:
            event, values = self.logic.read()
            if print_all_events: PrintEvent(event, values)
            if event in (None, 'Exit', 'Escape:27'):
                b = Quit()
                print(b)
                break
            elif event in ('-GRID_GRAPH-'):
                if do_mouse: Mouse('Click', event, values)
            elif '+UP' in event:
                if do_mouse: Mouse('Drag', event, values)
            elif '+MOVE' in event:
                if do_mouse: Mouse('Move', event, values)
            elif event == '__TIMEOUT__':
                pass
            elif event == 'Open a file  Ctrl-O':
                OpenFile()
            else: # Keyboard and MouseWheel
                if not do_keyboard: continue
                if len(event) == 1: Keyboard(event)
                else: Keyboard(event)
