import pandas as pd
from scipy.stats import poisson

df = pd.read_csv('traffic_data.csv')

# def get_congestion_prob(df):

#     vehicle_count = df.groupby('Weekday').count()
    
#     vehicleCountDF = vehicle_count[['Weight_kg']]
#     vehicleCountDF = vehicleCountDF.rename(columns={"Weight_kg": "Count"})


#     return vehicleCountDF['Count'] / (df.groupby('Weekday')['Second'].mean() / 60)

# print(get_congestion_prob(df))

