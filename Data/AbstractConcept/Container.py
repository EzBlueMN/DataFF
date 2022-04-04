from .AbstractConcept import AbstractConcept

class Container(AbstractConcept):
    def __init__(self, name='') -> None:
        super().__init__(name=name)
        self.parent = None
        self._children: List[AbstractConcept] = []

    def add(self, concept: AbstractConcept) -> None:
        self._children.append(concept)
        concept.parent = self
        self.update_depth_from_root()


    def remove(self, concept: AbstractConcept) -> None:
        self._children.remove(concept)
        concept.parent = None

    def is_container(self) -> bool:
        return True

    def update_depth_from_root(self) -> None:
        root = self.get_root()
        root.update_depth()
        
    def update_depth(self) -> None:
        if self.is_container():
            if len(self._children) > 0:
                for children in self._children:
                    children.depth = self.depth + 1
                    if children.is_container():
                        children.update_depth()

    def print_tree(self) -> None:
        print(self)
        for children in self._children:
            if children.is_container():
                children.print_tree()
            else:
                print(children)


    def operation(self) -> str:
        """
        The Container executes its primary logic in a particular way. It
        traverses recursively through all its children, collecting and summing
        their results. Since the Container's children pass these calls to their
        children and so forth, the whole object tree is traversed as a result.
        """

        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"
