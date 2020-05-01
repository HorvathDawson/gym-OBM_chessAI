import gym
from gym import wrappers
import numpy as np
import pygame
from pygame.locals import *
import time



class Chess:

    def __init__(self):
        self.env = gym.make('gym_OBM_chessAI:OBM_chessAI-v0')
        self._main_loop()

    def _main_loop(self):
        while True:
            time.sleep(1)
            self.env.render()
            moves = self.env._get_legal_move_list()
    		# No moves left
            if len(moves) == 0:
                self.env.reset()
            else:
                move = np.random.choice(moves)
                self.env.step(move)


if __name__ == "__main__":
    Chess()
