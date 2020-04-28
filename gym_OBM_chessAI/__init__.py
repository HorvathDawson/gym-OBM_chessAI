from gym.envs.registration import register

register(id='OBM_chessAI-v0',
    entry_point='gym_OBM_chessAI.envs:OBMchessEnv', 
)
