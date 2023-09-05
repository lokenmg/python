import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

#actividad 1
print(desc = reviews.description)

#actividad 2
print(first_description = reviews.description.iloc[0])

#actividad 3
print(first_row = first_row = reviews.iloc[0])

#actividad 4
print(first_descriptions = reviews.description.iloc[:10])

#actividad 5
print(sample_reviews = reviews.loc[[1, 2, 3, 5, 8]])

#actividad 6
cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]
print(df)

#actividad 7
cols_idx = [0, 11]
df = reviews.iloc[:100, cols_idx]
print(df)

#actividad 8
print(italian_wines = reviews[reviews.country == 'Italy'])

#actividad 9
print(top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]
)