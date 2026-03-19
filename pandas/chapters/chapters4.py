import pandas as pd 

reviews = pd.read_csv("pandas/data/winemag-data-130k-v2.csv")

print(reviews.info())

reviews_using_value_counts = reviews.points.value_counts()
print(reviews_using_value_counts.sort_values())

print()
print(reviews.groupby('points').points.count())

print(reviews.groupby('points').price.min())
print(reviews.groupby('points').price.max())

print(reviews.price.max())
print(reviews.price.min())

reviews_points_prices = reviews.groupby('points').price.agg(['max', 'min'])
print(reviews_points_prices)

print()
print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))

print()
print(reviews.groupby('country').price.agg([len, max, min]).sort_values(by='len', ascending=False))

