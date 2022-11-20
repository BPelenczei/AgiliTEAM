from __future__ import annotations
from drawable import Drawable
from direction import Direction
from steppable import Steppable
from interactable import Interactable
from drawingService import DrawingService
import abc


class Field(Steppable, Drawable):
    things: list[Interactable]
    neighbors = {
        'DOWN': None,
        'UP': None,
        'RIGHT': None,
        'LEFT': None,
    }
    position_x = None
    position_y = None

    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y
        self.things = []
        self.neighbors = {
            'DOWN': None,
            'UP': None,
            'RIGHT': None,
            'LEFT': None,
        }

    def step(self):
        for t in self.things:
            t.step()

    @abc.abstractmethod
    def accept(self, i: Interactable):
        pass

    @abc.abstractmethod
    def remove(self, i: Interactable):
        pass

    def get_neighbor(self, d: Direction) -> Field:
        return self.neighbors[d]

    def set_neighbor(self, d: Direction, f: Field) -> Field:
        self.neighbors[d] = f

    @abc.abstractmethod
    def draw(self, service: DrawingService):
        pass
