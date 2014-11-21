#!/usr/bin/env python
"""Noughts and Crosses Driver"""
import readline
from nac.model import NoughtsAndCrossesModel, ResultChecker, MoveResult
from nac.view import NoughtsAndCrossesView, BoardRenderer
from nac.controller import NoughtsAndCrossesController

def main():
    number_of_cells = 9
    winning_moves = [
        [ 0, 1, 2 ], [ 3, 4, 5 ], [ 6, 7, 8 ],
        [ 0, 3, 6 ], [ 1, 4, 7 ], [ 2, 5, 8 ],
        [ 0, 4, 8 ], [ 2, 4, 6 ]
    ]
    
    result_checker = ResultChecker(winning_moves, number_of_cells)
    model = NoughtsAndCrossesModel(result_checker, number_of_cells)

    board_renderer = BoardRenderer()
    view = NoughtsAndCrossesView(board_renderer)

    controller = NoughtsAndCrossesController(model, view)

    controller.reset()

    while True:
        try:
            thing = raw_input('> ')
            if thing.isdigit():
                controller.play_move(int(thing))
            elif thing == 'reset':
                controller.reset()
            elif thing == 'quit':
                controller.quit()
                break
        except KeyboardInterrupt:
            print
            controller.quit()
            break


if __name__ == '__main__':
    main()
