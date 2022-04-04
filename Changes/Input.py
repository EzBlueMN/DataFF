from __future__ import annotations
from abc import ABC, abstractmethod

class Input(ABC):
    @abstractmethod
    def __new__(self):
        pass

    def do(self) -> None:
        pass

class PrintEvent(Input):
    # def __new__(self, event, values) -> None: print(event, values)
    def __new__(self, event, values) -> None:
        if event not in values:
            self.logic.update_status(event)
        else:
            status = event + str(values[event])
            self.logic.update_status(status)

class Keyboard(Input):
    def __new__(self, event) -> None:
        if (':') in event:
            if event in ('Left:37', 'Up:38', 'Right:39', 'Down:40'):
                print(event.split(':')[0], 'key pressed!')
            else:
                print(event.split(':')[0], 'key released!')
        else:
            print(event, 'key pressed!')

class Mouse(Input):
    def __new__(self, action, event, values) -> None:
        if action not in ('Move', 'Drag', 'Click'): return

        if isinstance(event, str): graph = event
        else: graph = event[0]

        if action == 'Move': graph = graph[:-5]
        elif action == 'Drag': graph = graph[:-3]

        x = values[graph][0]
        y = values[graph][1]

        if action == 'Move': self.logic.mouse_move(x, y, graph)
        elif action == 'Drag': self.logic.mouse_drag(x, y, graph)
        else: self.logic.mouse_click(x, y, graph)

        show = False
        if show: print('[{}] Mouse moved to ({}, {}) inside {}'.format(window, x, y, graph))

class Quit(Input):
    def __new__(self) -> None: self.logic

class OpenFile(Input):
    def __new__(self) -> None:
        self.logic.open_file()