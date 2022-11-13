import numpy as np
from typing import List

from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.move import MovingTransformation
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.visualizable import Visualizable
from bosch_ASDIIE.AgiliTEAM.solid_version.core.interface.canvas import Canvas
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.map import MapSize, Coordinates


class Pacman(GameElement, Visualizable):

    def __init__(self,
                 body: List[Coordinates] = None,
                 starting_direction: KeyEvent = KeyEvent.RIGHT,
                 map_size: MapSize = None,
                 known_pos: List[List[Coordinates]] = None,
                 ):
        if known_pos is not None:
            self.known_pos = [item for sublist in known_pos for item in sublist]
        else:
            self.known_pos = []

        if map_size is None:
            map_size = MapSize(10, 10)

        if body is None:
            self.pos = self.generate_pos(1, map_size)
        else:
            self.pos = body

        self.moving_transformation = MovingTransformation(starting_direction, map_size)

    def generate_pos(self, num_of_pos: int, map_size: MapSize) -> List[Coordinates]:
        pos = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
        while pos in self.known_pos:
            pos = Coordinates(np.random.randint(map_size[0]), np.random.randint(map_size[1]))
        return [pos]

    def take_action(self, key_event: KeyEvent):
        self.moving_transformation.direction = key_event

    def get_pacman_position(self):
        return self.pos[0]

    def tick(self):
        self.pos = [self.moving_transformation(self.pos[0])]
        return True

    def draw(self, canvas: Canvas):
        canvas.draw_dots(self.pos, 'pacman')