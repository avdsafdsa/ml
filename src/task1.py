import pandas as pd
import os 
import numpy as np

df = pd.read_csv(os.getcwd() + "/1/car_fuel_efficiency_2026.csv")


#1
print(pd.__version__)
#2
row_count = df.shape[0]
print(row_count)

#3
print(df["fuel_type"].nunique())

#4

print(df.columns[df.isna().any()].shape[0])   

#5

print(df[df["origin"]=="Asia"]["fuel_efficiency_mpg"].max())

#6
col_name = "horsepower"
med = df[col_name].median()
moda = df[col_name].mode()[0]
med1 = df[col_name].fillna(moda).median()
print(med>med1)


#7
df = df[df["origin"]=="Asia"][["vehicle_weight","model_year"]]
df = df.head(7)

matrix1 = np.array(df)
martix1t = matrix1.transpose()
matrix1mult = np.matmul(martix1t, matrix1)
matrix1invert = np.linalg.inv(matrix1mult)
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
matrix1res1 = np.matmul(matrix1invert, martix1t)
matrix1res2 = np.matmul(matrix1res1, y)
print(matrix1res2.sum()) 



