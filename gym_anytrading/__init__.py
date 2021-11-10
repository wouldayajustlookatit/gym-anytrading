from pandas import DataFrame
from gym.envs.registration import register

df = DataFrame([])

register(
    id='forex-v0',
    entry_point='gym_anytrading.envs:ForexEnv',
    kwargs={
        'df': df,
        'window_size': 24,
        'frame_bound': (24, len(df))
    }
)

register(
    id='stocks-v0',
    entry_point='gym_anytrading.envs:StocksEnv',
    kwargs={
        'df': df,
        'window_size': 30,
        'frame_bound': (30, len(df))
    }
)
