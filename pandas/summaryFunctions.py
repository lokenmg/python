import pandas as pd
pd.set_option('display.max_rows', 5)
import numpy as np
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

print(reviews.points.describe())
print(reviews.taster_name.describe())
print(reviews.points.mean())
print(reviews.taster_name.unique())
print(reviews.taster_name.value_counts())

#maps
reviews_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)