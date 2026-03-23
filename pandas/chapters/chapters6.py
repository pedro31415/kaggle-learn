import pandas as pd

reviews  = pd.read_csv("pandas/data/winemag-data-130k-v2.csv")

reviews.rename(columns={'Unnamed: 0' :  'id_number'})
print(reviews.info())
print(reviews.infer_objects())