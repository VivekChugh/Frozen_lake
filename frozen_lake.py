import gym
import time
import random
import numpy as np


# PROGRAM PARAMETERS

# Episode parameters
episodes_num = 10000
max_steps_per_epsd = 100


lrn_rt = 0.1
dis_rt = 0.99 

# exploration-exploitation realated parameters
exp_rt = 1  
max_exp = 1
min_exp = 0.01
exp_rt_range = max_exp - min_exp
exp_decay_rt = 0.001 


# construct frozen lake env
fl_env = gym.make("FrozenLake-v0")

a_size = fl_env.action_space.n
s_size = fl_env.observation_space.n

#init Q table
qt = np.zeros((s_size, a_size))

# view how game score over time.
epsd_rewards = []

print("Train agent for 10000 episodes....")

for epsd in range(episodes_num): # loop for each episode
	
	#reset env variables for next episode
	s = fl_env.reset()
	epsd_over = False
	curr_epsd_rwd = 0

	for step in range(max_steps_per_epsd): # loop for each step in an epsd 

		# decide between exploitation and exploration
		thrsh_exp_rt = random.uniform(0,1)
		if exp_rt < thrsh_exp_rt:
			act = np.argmax(qt[s,:])	# exploitation			
		else:
			act = fl_env.action_space.sample()	# exploration
	
		# take action
		new_s, rwd, epsd_over, i = fl_env.step(act) 	

		# Update value of state-action pair in Q table
		qt[s,act] =  ((1 - lrn_rt) * qt[s,act]) + lrn_rt * (rwd + dis_rt * np.max(qt[new_s, :])) 

		s = new_s
		curr_epsd_rwd += rwd

		if epsd_over == True:
			break

	epsd_rewards.append(curr_epsd_rwd)
	
	# reduce exploration rate for next episode
	exp_rt = min_exp + (exp_rt_range * np.exp(-exp_decay_rt*epsd))

	if epsd%1000 == 0:
		print("Training episode num: " + str(epsd))

print_rwd = np.split(np.array(epsd_rewards),episodes_num/1000)

prv_rwd  = 0.0	
for r in print_rwd:
	curr_rwd = sum(r/1000) # avarage value
	if curr_rwd > prv_rwd:
		print("Avrage reward of 1000 episodes INCREASED to: " + str(curr_rwd)) 
	else:
		print("Avrage reward of 1000 episodes DECREASED to: " + str(curr_rwd))

	prv_rwd = curr_rwd	

##############################################################################
print()
print()
print("******************************************")
print("Play 10 games with trained agent")

for game in range(10):
	s = fl_env.reset()
	epsd_over = False

	for step in range(max_steps_per_epsd):
		act = np.argmax(qt[s,:])	# in actual game, agent always exploits
		new_s,rwd,epsd_over,i = fl_env.step(act)

		if epsd_over:
			if rwd == 1:
				print("Agent WON game " + str(game))
			else:
				print("Agent LOST game " + str(game))

			break

		s = new_s

fl_env.close()