import gym
import pygame
from gym import error, spaces, utils
from gym.utils import seeding
from pygame.locals import *

"""
    AGENT POLICY
    ------------
"""
# def make_random_policy(np_random):
# 	def random_policy(state):
# 		opp_player = -1
# 		moves = OBMchessEnv.AllowedMoves()
# 		# No moves left
# 		if len(moves) == 0:
# 			return 'resign'
# 		else:
# 			return np.random.choice(moves)
# 	return random_policy


"""
    CHESS GYM ENVIRONMENT CLASS
    ---------------------------
"""

class OBMchessEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    black = (0,0,0)
    white = (255,255,255)
    width, height = 640, 640
    gridWidth = 80
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen = self._initBoard(self.screen)

    def _initBoard(self, screen):
        for boardRow in range(8):
            for boardColumn in range(8):
                left = boardRow * self.gridWidth
                top  = boardColumn * self.gridWidth
                currentColour = self.white if (boardRow + boardColumn) % 2 == 0 else self.black
                pygame.draw.rect(screen,currentColour,[left,top, 80, 80])

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pygame.display.flip()
        pass
