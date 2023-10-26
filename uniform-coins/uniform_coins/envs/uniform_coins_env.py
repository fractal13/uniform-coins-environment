import gymnasium
import pygame
import numpy as np


class UniformCoinsEnv(gymnasium.Env):

    def __init__(self, render_mode=None, size=4):
        return

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        return observation, info

    def step(self, action):
        return observation, reward, terminated, False, info

    def render(self):
        if self.render_mode == "rgb_array":
            return self._render_frame()
        return

    def _render_frame(self):
        if self.window is None and self.render_mode == "human":
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((self.window_width, self.window_height))
        if self.clock is None and self.render_mode == "human":
            self.clock = pygame.time.Clock()

        return
    
    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()
        return
    


    
