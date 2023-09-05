import pandas as pd
##let's read the data from the csv file
wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=5)
##print the shape of the data
print(wine_reviews.shape)
##print the first 5 rows of the data
print("\n", wine_reviews.head())

