# import pandas as pd

# file = 'california_housing_train.csv'

# df = pd.read_csv(file)

# Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.

# print(df.median_house_value.mean()) #средняя


# avg = (df.loc[df.population < 500,['median_house_value']].mean())
# print(avg)


# avg = df[df['population']<500].median_house_value.mean()
# print(avg)


# Дан файл california_housing_train.csv.
# Найти максимальное значение переменной "households" в зоне минимального значения переменной "population" и сохраните это значение в переменную max_households_in_min_population.
# Используйте модуль pandas.


# min_population = df['population'].min()
# min_population_df = df[df['population'] == min_population]

# max_households_in_min_population = min_population_df['households'].max()
# print(max_households_in_min_population)





# min_population = df['population'].min()

# min_population_data = df[df['population'] == min_population]

# max_households_in_min_population = min_population_data['households'].max()

# print(max_households_in_min_population)


import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()