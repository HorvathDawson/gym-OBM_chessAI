import gym
from gym import wrappers
import pygame
from pygame.locals import *



class Chess:

    def __init__(self):
        self.env = gym.make('gym_OBM_chessAI:OBM_chessAI-v0')
        self._main_loop()

    def _main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    # if it is quit the game
                    pygame.quit()
                    exit(0)
            self.env.render()


if __name__ == "__main__":
    Chess()
