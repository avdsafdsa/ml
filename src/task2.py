import pandas as pd
import os 
import numpy as np


df = pd.read_csv(os.getcwd() + "/1/car_fuel_efficiency_2026.csv")
df=df[["vehicle_weight","model_year","fuel_efficiency_mpg","engine_displacement","horsepower"]]
print(df.isna().sum().to_string())
print(df["horsepower"].median())