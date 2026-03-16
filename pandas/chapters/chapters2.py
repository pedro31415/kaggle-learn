import pandas as pd

wine_reviews = pd.read_csv("pandas/data/winemag-data-130k-v2.csv")

print(wine_reviews.country)
print()
print(wine_reviews['country'])
print(wine_reviews['country'][10])
print(len(wine_reviews['country']))
print()
print(wine_reviews.iloc[4])

unique_values_country = wine_reviews['country'].unique()
print(unique_values_country)
print(len(unique_values_country))
print(unique_values_country[14])
print(unique_values_country)


# using loc and iloc
print(wine_reviews.iloc[:, 1])
print(wine_reviews.set_index('country'))
print(wine_reviews['country'] == 'US')

count = 0
i = 0

while i < len(wine_reviews.country):
    if wine_reviews.loc[i, 'country'] == 'US':
        count += 1
    i += 1
print(f'Wines of US: {count}')

all_wines_reviews = len(wine_reviews['country'])
print(all_wines_reviews)

wine_of_US_percentage = (count * 100) / all_wines_reviews
print(f'percentage -> {wine_of_US_percentage}')


print()
print(wine_reviews.loc[wine_reviews.country.isin(['Italy', 'Hungary'])])

result_wine = wine_reviews.loc[(wine_reviews.country == 'Italy') | (wine_reviews.points >= 90)]
print(result_wine)

print()
print()
print(wine_reviews.describe())