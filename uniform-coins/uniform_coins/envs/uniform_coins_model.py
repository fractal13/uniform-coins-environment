import numpy as np

class UniformCoinsState:
    """A collection of N coins. Turn over coins until all coins are tails, or all coins are heads."""

    def __init__(self, size=5):
        self._coins = np.random.zeros(size, dtype=np.int8)
        return

    def reset(self, seed=None):
        if seed is not None:
            np.random.seed(seed)
        self._coins = np.random.randint(2, size=size, dtype=np.int8)
        return self._coins
    
class UniformCoinsModel:

    def ACTIONS(cls, state):
        actions = []
        ?
        return actions

    def RESULT(cls, state, action):
        state1 = ?
        return state1

    def GOAL_TEST(cls, state):
        return False

    def STEP_COST(cls, state, action, state1):
        cost = 1.0
        return cost

    def HEURISTIC(cls, state):
        estimated_cost = 0.0
        return estimated_cost

