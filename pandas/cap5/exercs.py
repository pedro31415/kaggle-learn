import pandas as pd

reviews = pd.read_csv('pandas/data/winemag-data-130k-v2.csv')
print(reviews.info())

# 1 exercise 
dtype = reviews.points.dtype
print(dtype)

# 2 exercise
point_strings = reviews.points.astype('str')
print(point_strings)

# 3 exercise 
n_missing_prices = reviews.price.isnull().sum()
print(n_missing_prices)