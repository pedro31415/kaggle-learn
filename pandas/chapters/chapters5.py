import pandas as pd

reviews  = pd.read_csv("pandas/data/winemag-data-130k-v2.csv")

print(reviews.price.dtype)
print(reviews.country.describe())
print(reviews.price.describe())
print(reviews.country.dtype)
print()
print(reviews.describe())
print(reviews.dtypes)

print()
print(reviews[pd.isnull(reviews.country)])
reviews_changed = reviews

reviews_changed.region_2.fillna("Unknown")
print(reviews_changed.region_2.fillna("Unknown"))

print(reviews.region_2)

print(reviews.info())
print(reviews_changed.taster_twitter_handle)

print(reviews_changed.taster_twitter_handle.replace('@vossroger', '@pedrinho'))


