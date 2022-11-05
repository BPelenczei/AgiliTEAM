from typing import List
import numpy as np

from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_event import KeyEvent
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element import GameElement
from bosch_ASDIIE.AgiliTEAM.solid_version.core.visualizable import Visualizable
from bosch_ASDIIE.AgiliTEAM.solid_version.core.canvas import Canvas
from bosch_ASDIIE.AgiliTEAM.solid_version.core.map import MapSize, Coordinates


class Ghosts(GameElement, Visualizable):

    def take_action(self, key_event: KeyEvent):
        pass

    def tick(self) -> bool:
        pass

    def draw(self, canvas: Canvas):
        pass
