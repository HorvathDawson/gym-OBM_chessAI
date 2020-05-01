import gym
import pygame
import numpy as np
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

    def __init__(self):
        self.env = chess.Board()
        self.reward_lookup = {
            'check': 0.05,
            'mate': 100.0,
            'stalemate': 0.0,
            'p': 0.1,
            'n': 0.3,
            'b': 0.3,
            'r': 0.5,
            'q': 0.9,
            '1': 0.1,  # Promotion to pawn
            '2': 0.1,  # Promotion to knight
            '3': 0.1,  # Promotion to bishop
            '4': 0.1,  # Promotion to rook
            '5': 0.1   # Promotion to queen
        }
        self.piece_lookup = {
            'p': -1,#lower case is black variant
            'n': -2,
            'b': -3,
            'r': -4,
            'q': -5,
            'k': -6,
            'P': 1, #upper case is white variant
            'N': 2,
            'B': 3,
            'R': 4,
            'Q': 5,
            'K': 6
        }

    def step(self, action):
        """
        input: action in UCI format (i.e. 'a2a4')
        :return:
            state: numpy array:  [[board with all pieces represented as integers], [list of legal moves]]
            reward: Float value
            is_terminated: if game has ended in checkmate, stalemate, insufficient material, seventyfive-move rule,
            info: dictionary containing any debugging information
                           fivefold repetition, or a variant end condition.
        """
    # -------------------------------------------
    # handle the capture rewards
    # -------------------------------------------
        #set reward to 0 initially
        reward = 0.0
        #get piece map and the square the new move is going to
        piece_map = self.env.piece_map()
        to_square = chess.Move.from_uci(action).to_square
        # check if their is a piece on the destination of the move if there is then
        if to_square in piece_map.keys():
            # find what piece is captured
            captured_piece = piece_map[to_square].symbol()
            # get reward for capturing the piece
            reward = self.reward_lookup[captured_piece.lower()]

        #check if the move resulted in a promotion if it did then get the reward associated with it
        promotion = chess.Move.from_uci(action).promotion
        if promotion is not None:
            reward += self.reward_lookup[str(promotion)]

    # ---------------------------------------------
    # complete move
    # ---------------------------------------------
        self.env.push_uci(action)
    # -------------------------------------------
    # handle the end condition  rewards
    # -------------------------------------------
        #_update_reward function based on end condtions if in check, mate, stalemate, or draw
        if self.env.is_check():
            reward += self.reward_lookup['check']
        end_game_result = self.env.result()
        if '1-0' in end_game_result or '0-1' in end_game_result:
            reward = self.reward_lookup['mate']
        elif '1/2-1/2' in end_game_result:
            reward = self.reward_lookup['stalemate']
    # -------------------------------------------
    # get state info
    # -------------------------------------------
        # get current state
        state = _get_array_state(piece_map)
        # check end condition
        is_terminated = self.env.is_game_over()
        info = {}
        return state, reward, is_terminated, info

    def set_fen(self, fen):
        self.env.set_fen(fen)
        return self._get_array_state()

    def reset(self):
        """
        :return: current state as numpy array
        """
        self.env.reset()
        state = self._get_array_state()
        return state

    def render(self, mode='human', close=False):
        piece_map = self.env.piece_map()
        state = self._get_array_state(piece_map)
        print(self.env)
        print(state[0])
        print(state[1])

    def _get_legal_move_list(self):
        a = list(enumerate(self.env.legal_moves))
        b = [x[1] for x in a]
        c = []
        i = 0
        for item in b:
            c.append(str(b[i]))
            i += 1
        return c

    def _get_array_state(self, piece_map):
        """
        input: String from chess.Board.board_fen().  Ex.: 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        Each lower-case character is black piece, and upper case is white piece.
        :return: 8x8 numpy array.  Current player's pieces are positive integers, enemy pieces are negative.
        """
        state = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0]])

        for square, piece in piece_map.items():
            col = int((square) / 8)
            row = int((square) % 8)
            state[col][row] = self.piece_lookup[piece.symbol()]

        #reverse which ever pieces are neg/pos to make active piece positive if necessary
        if (self.env.turn == chess.BLACK):
            state *= -1
        #get legal moves in current state
        legal_moves = self._get_legal_move_list()
        return [state, legal_moves]
