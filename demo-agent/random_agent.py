#!/usr/bin/env python3

import gymnasium as gym
import uniform_coins
import random

env = gym.make('uniform_coins/UniformCoins-v0', render_mode=None)
observation, info = env.reset()
state = uniform_coins.UniformCoinsState()
state.observation = observation

terminated = truncated = False
while not (terminated or truncated):
    action = random.choice(uniform_coins.UniformCoinsModel.ACTIONS(state))
    observation, reward, terminated, truncated, info = env.step(action)
    state.observation = observation
    print(state)

env.close()

