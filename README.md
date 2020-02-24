# Frozen_lake (https://gym.openai.com/envs/FrozenLake-v0/)
This code implements a reinforcement learning agent. 
Agent uses policy iteration at each step to choose policy that can maximize reward.
policy iteration approach works fine becuase of limited size of Q-table.


Agent plays 10000 episodes calculating avarage reward every 1000 episodes.
Then it plays 10 games to check how well it has trained.

C:\Users\VCHUGH\Desktop\RL>python frozen_lake.py
Train agent for 10000 episodes....
Training episode num: 0

Training episode num: 1000

Training episode num: 2000

Training episode num: 3000

Training episode num: 4000

Training episode num: 5000

Training episode num: 6000

Training episode num: 7000

Training episode num: 8000

Training episode num: 9000

Avrage reward of 1000 episodes INCREASED to: 0.04900000000000004

Avrage reward of 1000 episodes INCREASED to: 0.19700000000000015

Avrage reward of 1000 episodes INCREASED to: 0.4020000000000003

Avrage reward of 1000 episodes INCREASED to: 0.5650000000000004

Avrage reward of 1000 episodes INCREASED to: 0.5850000000000004

Avrage reward of 1000 episodes INCREASED to: 0.6720000000000005

Avrage reward of 1000 episodes DECREASED to: 0.6610000000000005

Avrage reward of 1000 episodes INCREASED to: 0.6690000000000005

Avrage reward of 1000 episodes DECREASED to: 0.6490000000000005

Avrage reward of 1000 episodes INCREASED to: 0.6910000000000005


******************************************

Play 10 games with trained agent

Agent WON game 0

Agent LOST game 1

Agent WON game 2

Agent WON game 3

Agent WON game 4

Agent WON game 5

Agent WON game 6

Agent WON game 7

Agent LOST game 8

Agent WON game 9

