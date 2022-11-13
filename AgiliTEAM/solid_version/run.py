import curses
from argparse import ArgumentParser

from bosch_ASDIIE.AgiliTEAM.solid_version.core.game import Game
from bosch_ASDIIE.AgiliTEAM.solid_version.core.key_interaction.key_listener import KeyListener
from bosch_ASDIIE.AgiliTEAM.solid_version.core.pacman_game_state import PacmanGameState
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.pacman import Pacman
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.pellets import Pellets
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.ghosts import Ghosts
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.walls import Walls
from bosch_ASDIIE.AgiliTEAM.solid_version.core.display.visualizer import Visualizer
from bosch_ASDIIE.AgiliTEAM.solid_version.gui.console_canvas import ConsoleCanvas
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.map import MapSize
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.config_loader import ConfigLoader
from bosch_ASDIIE.AgiliTEAM.solid_version.core.display.screen import Screen
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.score_counter import ScoreCounter
from bosch_ASDIIE.AgiliTEAM.solid_version.core.game_element.defeat_checker import DefeatChecker
from bosch_ASDIIE.AgiliTEAM.solid_version.core.misc.custom_argument_parser import CustomArgParser


def main():
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--gui", type=str, default=GUI)
    arg_parser.add_argument("--map_width", type=int, default=WIDTH)
    arg_parser.add_argument("--map_height", type=int, default=HEIGHT)
    arg_parser.add_argument("--difficulty", type=float, default=DIFFICULTY)
    arg_parser.add_argument("--num_pellets", type=int, default=PELLETS)
    arg_parser.add_argument("--num_ghosts", type=int, default=GHOSTS)
    arg_parser.add_argument("--base_score", type=int, default=BASE_SCORE)
    arg_parser.add_argument("--ghost_step_confidence", type=float, default=STEP_CONFIDENCE)
    args = arg_parser.parse_args()

    screen = Screen()
    curses.cbreak()

    key_listener = KeyListener()
    key_listener.start(screen)

    pacman = Pacman(map_size=MapSize(HEIGHT, WIDTH))
    pellets = Pellets(map_size=MapSize(HEIGHT, WIDTH), num_pellets=args.num_pellets, known_pos=[pacman.pos])
    ghosts = Ghosts(map_size=MapSize(HEIGHT, WIDTH), num_ghosts=args.num_ghosts, known_pos=[pacman.pos, pellets.pos],
                    step_confidence=args.ghost_step_confidence)
    score_counter = ScoreCounter(base_score=args.base_score, difficulty=args.difficulty, pacman=pacman, pellets=pellets)
    defeat_checker = DefeatChecker(pacman=pacman, ghosts=ghosts)

    if args.gui == 'console':
        canvas = ConsoleCanvas(MapSize(args.map_width, args.map_height), screen)
    else:
        raise NotImplementedError

    visualizer = Visualizer([ghosts, pellets, pacman], canvas)
    start_game_state = PacmanGameState([pacman, pellets, ghosts, score_counter, defeat_checker])
    game = Game(key_listener, start_game_state, visualizer, args.difficulty)
    game.run()

    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()


if __name__ == "__main__":
    main()
