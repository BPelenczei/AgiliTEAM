import unittest

from core.key_interaction.key_event import KeyEvent
from core.pacman_game_state import PacmanGameState
from core.game_element.pacman import Pacman
from core.misc.map import Coordinates, MapSize


class GameStateTest(unittest.TestCase):
    def test_WhenOneStep_IsTerminatedFalse(self):
        pacman_game_state = PacmanGameState([])
        pacman_game_state.step()
        self.assertFalse(pacman_game_state.is_terminated(),
                         "The initialized game should not step into terminated state.")

    def test_PacmanStepFunction(self):
        pacman = Pacman(body=[Coordinates(5, 5)], map_size=MapSize(10, 10))
        test_game_state = PacmanGameState([pacman])
        test_game_state.take_action(KeyEvent.UP)
        test_game_state.step()
        self.assertFalse(pacman.get_pacman_position() == [Coordinates(5, 6)], "Error during step, value mismatch")

    def test_PacmanCanNotLeaveThePitch_TopLeftCornerPos(self):
        pacman = Pacman(body=[Coordinates(1, 1)], map_size=MapSize(3, 3))
        test_game_state = PacmanGameState([pacman])
        test_game_state.take_action(KeyEvent.UP)
        test_game_state.step()
        test_game_state.take_action(KeyEvent.LEFT)
        test_game_state.step()
        self.assertFalse(pacman.get_pacman_position() == [Coordinates(0, 0)],
                         "Error during step, value mismatch")