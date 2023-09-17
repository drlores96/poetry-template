"""
dummy.py
========

Dummy module with a dummy dataclass.
"""


class Dummy:
    a: int
    b: int

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a + b
