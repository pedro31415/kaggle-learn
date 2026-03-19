import pandas as pd
import numpy as np

reviews = pd.read_csv("pandas/data/winemag-data-130k-v2.csv")

print(reviews.describe())

print(reviews.info())

reviews_news = reviews.drop(columns=['Unnamed: 0'])
print(reviews.points.mean())

print(reviews.points)
print(reviews.points.unique())
print(reviews.points.unique().sort())
print(np.sort(reviews.points.unique()))
print()
print(reviews.points.value_counts(ascending=True))