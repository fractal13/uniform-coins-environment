from gymnasium.envs.registration import register

register(
     id="uniform_coins/UniformCoins-v0",
     entry_point="uniform_coins.envs:UniformCoinsEnv",
     max_episode_steps=50,
)
