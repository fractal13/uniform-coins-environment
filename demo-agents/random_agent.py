#!/usr/bin/env python3

import gymnasium as gym
import uniform_coins
import random

def agent_function(state):
    """
    state: A uniform_coins.UniformCoinsState object. The current state of the environment.
    
    returns: An integer, the coin to turn over.
    """
    action = random.choice(uniform_coins.UniformCoinsModel.ACTIONS(state))
    return action

def main():
    env = gym.make('uniform_coins/UniformCoins-v0', render_mode=None, coin_count=3)
    observation, info = env.reset()
    state = uniform_coins.UniformCoinsState()
    state.observation = observation
    
    terminated = truncated = False
    print(f"Current state: {state}")
    while not (terminated or truncated):
        print()
        action = agent_function(state)
        print(f"Action: turn coin {action}.")
        observation, reward, terminated, truncated, info = env.step(action)
        state.observation = observation
        print(f"Current state: {state}")

    env.close()
    return

if __name__ == "__main__":
    main()
    

