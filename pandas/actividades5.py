import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
#actividad 1
print(point_strings = reviews.points.astype(str))
#actividad 2
print(point_strings = reviews.points.astype(str))

#actividad 3
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
print(n_missing_prices)
#actividad 4
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
print(reviews_per_region)