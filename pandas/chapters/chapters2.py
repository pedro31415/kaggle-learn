import pandas as pd

wine_reviews = pd.read_csv("pandas/data/winemag-data-130k-v2.csv")

print(wine_reviews.country)
print()
print(wine_reviews['country'])
print(wine_reviews['country'][10])

unique_values_country = wine_reviews['country'].unique()
print(unique_values_country)
print(len(unique_values_country))