
from .chooseenv import make
from copy import deepcopy
from .common import *


class SnakeEnvWrapper():
    def __init__(self, mode='OneVsOne-v0'):
        self.env = make("snakes_30v30", conf=None)
        self.states = None
        self.ctrl_agent_index = list(range(0, 30))
        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,\
        #                          24, 25, 26, 27, 28, 29]
        self.obs_dim = 26
        self.height = self.env.board_height
        self.width = self.env.board_width
        self.episode_reward = np.zeros(6)

    def act(self):
        return self.env.act(self.states)

    def reset(self):
        states = self.env.reset()
        # print(states)
        # print('*****')
        length = []
        obs = process_obs_joint(states[0])
        # print('{} is obs'.format(obs))
        # print(obs.shape)
        self.states = deepcopy(states)
        legal_action = get_legal_actions(states[0])
        info = {}
        info ["legal_action"] = legal_action
        # print(obs.shape)
        return obs, info

    def step(self, actions):
        next_state, reward, done, _, info = self.env.step(self.env.encode(actions))
        next_obs = process_obs_joint(next_state[0])
        # reward shaping
        step_reward = get_reward_joint(reward, next_state[0], done)
        length = []
        for i in range(2,62):
            length.append(len(next_state[0][i]))
        info ["length"] = length
        legal_action = get_legal_actions(next_state[0])
        info ["legal_action"] = legal_action
        return next_obs, step_reward, done, info

    def render(self):
        self.env.render()


