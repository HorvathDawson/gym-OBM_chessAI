import gym
import pygame
from gym import error, spaces, utils
from gym.utils import seeding
from pygame.locals import *

try:
    import chess
except ImportError as e:
    raise error.DependencyNotInstalled(
        "{}.  (HINT: see README for python-chess installation instructions".format(e))

# """
#     AGENT POLICY
#     ------------
# """

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


# """
#     CHESS GYM ENVIRONMENT CLASS
#     ---------------------------
# """

class OBMchessEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    # board structure
    black = (0,0,0)
    white = (255,255,255)
    width, height = 640, 640
    gridWidth = 80
    # piece icons
    bishopB = pygame.image.load("resources/chesspieces/bishopB.png")
    bishopW = pygame.image.load("resources/chesspieces/bishopW.png")
    kingB = pygame.image.load("resources/chesspieces/kingB.png")
    kingW = pygame.image.load("resources/chesspieces/kingW.png")
    knightB = pygame.image.load("resources/chesspieces/knightB.png")
    knightW = pygame.image.load("resources/chesspieces/knightW.png")
    pawnB = pygame.image.load("resources/chesspieces/pawnB.png")
    pawnW = pygame.image.load("resources/chesspieces/pawnW.png")
    queenB = pygame.image.load("resources/chesspieces/queenB.png")
    queenW = pygame.image.load("resources/chesspieces/queenW.png")
    rookB = pygame.image.load("resources/chesspieces/rookB.png")
    rookW = pygame.image.load("resources/chesspieces/rookW.png")


    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.board = chess.Board()
        self.screen = self._drawBoard(self.screen)

    def _drawBoard(self, screen):
        for boardRow in range(8):
            for boardColumn in range(8):
                # set background colour
                left = boardRow * self.gridWidth
                top  = boardColumn * self.gridWidth
                currentColour = self.white if (boardRow + boardColumn) % 2 == 0 else self.black
                pygame.draw.rect(screen,currentColour,[left,top, 80, 80])
                # add piece if required

    def step(self, action):



        pass

    def reset(self):
        pass

    def render(self, mode='human', close=False):
        pygame.display.flip()
        # for event in pygame.event.get():
        #     if event.type==pygame.QUIT:
        #         # if it is quit the game
        #         pygame.quit()
        #         exit(0)
        pass
