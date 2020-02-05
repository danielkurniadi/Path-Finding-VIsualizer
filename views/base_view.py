""" Modules containing BaseView class definition
"""

class BaseView(object):
    """ Abstraction class for View subclass
    """

    __abstract__ = True

    def __init__(self):
        self.reset()

    def reset(self):
        raise NotImplementedError("Please implement `reset()` for your View Class")

