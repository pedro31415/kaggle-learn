import pandas as pd

# 1 exercise
reviews = pd.read_csv('pandas/data/winemag-data-130k-v2.csv')

print(reviews.head())

print(reviews.description)

desc = reviews.description 
print(desc)

# 2 exercise 
first_description = desc[0]
print()
print(first_description)

# 3 exercise 
indices = [1,2,3,5,8]
sample_reviews = reviews.loc[indices]
print(sample_reviews)

# 4 exercise 
indices = [0,1,10,100]
new_df = reviews.loc[indices][['country', 'province', 'region_1', 'region_2']]
print()
print(new_df)

# 5 exercise 
print(reviews[reviews['country'] == 'Italy'])