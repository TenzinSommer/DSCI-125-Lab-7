import pandas as pd
import numpy as np
from scipy.stats import pearsonr

df = pd.read_csv('traffic_data_f1.csv')

def get_correlation(df):
    result = []
    
    for vehicle_type, group in df.groupby("Type"):
        corr_speed_weight = group["Speed_kmh"].corr(group["Weight_kg"])
        corr_speed_wheelbase = group["Speed_kmh"].corr(group["Wheelbase_mm"])
        
        result.append([vehicle_type, "Speed_kmh", "Weight_kg", round(corr_speed_weight, 4)])
        result.append([vehicle_type, "Speed_kmh", "Wheelbase_mm", round(corr_speed_wheelbase, 4)])
    
    return pd.DataFrame(result, columns=["type", "speed", "factor", "correlation"])


print(get_correlation(df))