import numpy as np
from scipy.stats import *
from random import random

def get_frequency(bet, hours):
	hour_wins = []
	for i in range(hours):
		wins = 0
		for j in range(120):
			spin = random()*37//1
			if (1 <= spin) & (spin <= 12):
				wins += bet['1st12']
			if (13 <= spin) & (spin <= 24):
				wins += bet['2nd12']
			if (25 <= spin) & (spin <= 36):
				wins += bet['3rd12']
			if spin % 2 == 0:
				wins += bet['even']
			else:
				wins += bet['odd']
		hour_wins.append(wins)

	return np.mean(hour_wins)

def get_win_range_prob(bet, hours, low, high):
	freq = get_frequency(bet, hours)
	return (poisson.cdf(freq, low) - poisson.cdf(freq, high)).round(4)

bet = {
    '1st12': 1,
    '2nd12': 0,
    '3rd12': 0,
    'even': 0,
    'odd': 0,
}
print(f'get_frequency:\
	  \nexpected: ~38.89\
	  \nactual:{get_frequency(bet, 10000)}\n')

print(f'get_win_range_prob:\
	  \nexpected: ~0.0477\
	  \nactual:{get_win_range_prob(bet, 10000, 50, 100)}\n')