import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
#actividad 1
renamed = renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))
print(renamed)


#actividad 3
gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"
combined_products = pd.concat([gaming_products, movie_products])
print(combined_products)
#actividad 4
powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))
print(powerlifting_combined)