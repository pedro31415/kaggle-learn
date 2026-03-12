import pandas as pd

print(pd.__version__)

# creating dataframe

new_dataframe= pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product b'])

print(new_dataframe)
print()
print(new_dataframe['Bob'])

# reading data
wine_reviews = pd.read_csv("pandas/data/winemag-data-130k-v2.csv")
print(wine_reviews.head(8))
print()
print(wine_reviews.shape)
print(wine_reviews.info())