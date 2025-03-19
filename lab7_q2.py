import pandas as pd
import numpy as np
from scipy.stats import expon

df = pd.read_csv('traffic_data.csv')

def get_minute_gap_prob(df, weekday):
	# seconds = df.loc[df['Weekday'] == weekday]['Second'].to_list()
	# wait_times = []
	# for i in range(len(seconds) - 1):
	# 	wait_times.append(seconds[i+1] - seconds[i])
	# avg_wait = np.mean(wait_times)

	cars = len(df.loc[df['Weekday'] == weekday])
	avg_wait = (60*24) / cars

	return 1 - expon.pdf(1, scale= 1 / avg_wait)

# print(df.loc[df['Weekday'] == "Fri"]['Second'].to_list())
print (get_minute_gap_prob(df, "Fri"))