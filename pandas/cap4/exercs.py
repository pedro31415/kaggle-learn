import pandas as pd

# 1 exercise
reviews = pd.read_csv('pandas/data/winemag-data-130k-v2.csv')
print(reviews.info())

reviews_written = reviews.groupby('taster_twitter_handle').country.agg(len)
print(reviews_written)

# 2 exercise 
best_rating_per_price = reviews.groupby('price').points.agg('max').sort_index()
print(best_rating_per_price)

# best answer
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
print(best_rating_per_price)

# 3 exercise 
price_extremes = reviews.groupby('variety').price.agg(['min', 'max'])
print(price_extremes)
