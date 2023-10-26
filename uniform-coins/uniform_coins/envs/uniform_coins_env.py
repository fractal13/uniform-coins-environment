import gymnasium
import pygame
import numpy as np
from gymnasium import spaces
from uniform_coins.envs.uniform_coins_model import UniformCoinsModel
from uniform_coins.envs.uniform_coins_model import UniformCoinsState

class UniformCoinsEnv(gymnasium.Env):

    def __init__(self, render_mode=None, coin_count=4):
        self.render_mode = render_mode
        self.coin_count = coin_count
        self.action_space = spaces.Discrete(coin_count)
        self.observation_space = spaces.Box(0, 1, shape=(coin_count,), dtype=np.int8)
        return

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = UniformCoinsState(self.coin_count)
        self.state.randomize(seed)

        observation = self.state.observation
        info = {}
        return observation, info

    def step(self, action):
        state = self.state
        state1 = UniformCoinsModel.RESULT(state, action)
        self.state = state1
        
        observation = self.state.observation
        reward = UniformCoinsModel.STEP_COST(state, action, state1)
        terminated = UniformCoinsModel.GOAL_TEST(state1)
        info = {}
        return observation, reward, terminated, False, info

    def render(self):
        # if self.render_mode == "rgb_array":
        #     return self._render_frame()
        return

    def _render_frame(self):
        # if self.window is None and self.render_mode == "human":
        #     pygame.init()
        #     pygame.display.init()
        #     self.window = pygame.display.set_mode((self.window_width, self.window_height))
        # if self.clock is None and self.render_mode == "human":
        #     self.clock = pygame.time.Clock()

        return
    
    def close(self):
        # if self.window is not None:
        #     pygame.display.quit()
        #     pygame.quit()
        return
    


    
