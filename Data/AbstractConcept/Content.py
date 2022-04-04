from .AbstractConcept import AbstractConcept

class Content(AbstractConcept):
    """
    The Content class represents the end objects of a composition. A Content can't
    have any children.

    Usually, it's the Content objects that do the actual work, whereas Composite
    objects only delegate to their sub-Concepts.
    """

    def __init__(self, name=''):
        super().__init__(name=name)

    def operation(self) -> str:
        return "Content"
