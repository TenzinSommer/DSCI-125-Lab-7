import pandas as pd
import numpy as np
from scipy.stats import expon


def get_minute_gap_prob(df, weekday):
	seconds = df.loc[df['Weekday'] == weekday]['Second'].to_list()
	wait_times = []
	for i in range(len(seconds) - 1):
		wait_times.append(seconds[i+1] - seconds[i])

	avg_wait = np.mean(wait_times)


	return round(1 - expon.cdf(60, scale= avg_wait), ndigits = 4)

