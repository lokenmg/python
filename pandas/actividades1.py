## actividad 1
import pandas as pd
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

#Actividad 2
fruit_sales = pd.DataFrame({'Apples': [35,41],
                            'Bananas': [21,34]},
                            index=['2017 Sales', '2018 Sales'])

#Actividad 3
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', "Spam"], name='Dinner')

#Actividad 4
reviews = pd.read_csv("winemag-data_first150k.csv", index_col=0)

#Actividad 5
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals.to_csv("cows_and_goats.csv")
