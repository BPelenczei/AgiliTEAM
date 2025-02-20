from TeamSix.solid_version.interfaces.field import Field
from TeamSix.solid_version.interfaces.interactable import Interactable
from TeamSix.solid_version.display.drawingService import DrawingService


class Coin_holder(Field):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.things = []
        self.neighbors = {
            'DOWN': None,
            'UP': None,
            'RIGHT': None,
            'LEFT': None,
        }

    def accept(self, i: Interactable):
        for thing in self.things:
            i.collide_with(thing)
        self.things.append(i)
        i.field = self

    def remove(self, i: Interactable):
        self.things.remove(i)

    def draw(self, service: DrawingService):
        service.draw_field(self.position_x, self.position_y, 'blank')
        for t in self.things:
            t.draw(service)
