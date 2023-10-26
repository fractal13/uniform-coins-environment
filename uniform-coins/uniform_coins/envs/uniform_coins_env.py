import gymnasium
import pygame
import numpy as np
import uniform_coins_model

class UniformCoinsEnv(gymnasium.Env):

    def __init__(self, render_mode=None, size=4):
        self.render_mode = render_mode
        self.size = size
        return

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = uniform_coins_model.UniformCoinsState(self.size)
        self.state.randomize(seed)

        observation = self.state
        info = {}
        return observation, info

    def step(self, action):
        state = self.state
        state1 = uniform_coins_model.UniformCoinsModel.RESULT(state, action)
        self.state = state1
        
        observation = self.state
        reward = uniform_coins_model.UniformCoinsModel.STEP_COST(state, action, state1)
        terminated = uniform_coins_model.UniformCoinsModel.GOAL_TEST(state1)
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
    


    
