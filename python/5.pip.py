import pandas
house = pandas.read_csv('boston.csv')
print(house)
print(house.head(2))
print(house.describe())