import pandas as pd

# 1 exercise
reviews = pd.read_csv('pandas/data/winemag-data-130k-v2.csv')

median_points = reviews.points.median()
print(median_points)


# 2 exercise 
countries = reviews.country.unique()
print(countries)

# 3 exercise 
reviews_per_country = reviews.country.value_counts()
print(reviews_per_country)

# 4 exercise 
avg_price = reviews.price.mean()
centered_price = reviews['price'].map(lambda x: x - avg_price)
print(centered_price)