from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class AbstractConcept(ABC):
    """
    The base Concept class declares common operations for both simple and
    complex objects of a composition.
    """

    def __init__(self, name=''):
        self._name = name
        self._depth = 0

    def get_root(self) -> AbstractConcept:
        concept = self._parent
        if concept == None:
            return self
        while True:
            if concept._parent == None:
                break
            concept = concept._parent
        return concept

    def __str__(self):
        return self._name

    @property
    def depth(self) -> int:
        return self._depth

    @property
    def name(self) -> str:
        return self._name

    @property
    def parent(self) -> AbstractConcept:
        return self._parent

    @depth.setter
    def depth(self, depth: int):
        self._depth = depth

    @name.setter
    def name(self, name: str):
        self._name = name

    @parent.setter
    def parent(self, parent: AbstractConcept):
        self._parent = parent

    def add(self, concept: AbstractConcept) -> None:
        pass

    def remove(self, concept: AbstractConcept) -> None:
        pass

    def is_container(self) -> bool:
        return False

    def print_tree(self) -> None:
        pass

    @abstractmethod
    def operation(self) -> str:
        pass