# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы




import pandas as pd
# california_housing_train.csv
file = 'california_housing_train.csv'

df = pd.read_csv(file)
# print(df.head())
# # print(df.tail())
# print(df.shape)
# print(df.dtypes)

# задача 59
# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000

# print(df.isnull().sum()) #анализ пустых ячеек
# print(df.loc[df.median_income < 2, ['median_income', 'median_house_value']]) # 2. Показать median_house_value где median_income < 2
# print(df['longitude'],['latitude']) # 3. Показать данные в первых 2 столбцах
# print(df.iloc[:, 0:2]) # 3. Показать данные в первых 2 столбцах
# df.to_excel('file.xlsx')
print('*' * 25)
# df2 = df.iloc[:, 0:2]
# print(df2.head)
# df.to_excel('file2.xlsx')
# print(df.loc[df.housing_median_age < 20, ['housing_median_age','median_house_value']])
# print(df.loc[(df.housing_median_age < 20) & (df.median_house_value > 70000), ['housing_median_age','median_house_value']]) # 4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000

# Задача №61. Решение в группах
# 1. Определить какое максимальное и минимальное
# значение median_house_value
# 
# 

# print(df.median_house_value.max()) #максимальая
# print(df.median_house_value.min()) #минимальная
# print(df.median_house_value.mean()) #средняя
# print(df.median_house_value.median()) #медианное значение
# print('*' * 25)

# 2. Показать максимальное median_house_value, где median_income = 3.1250
# print(df.loc[df.median_income == 3.1250, ['median_house_value']].max())
# print('*' * 25)

# 3. Узнать какая максимальная population в зоне минимального значения median_house_value
# print(df.loc[df.median_house_value == 14999.0,['population']].max())
# print(df.loc[df.median_house_value == df.median_house_value.min(), ['median_house_value','population']])
# print('*' * 25)
# print(df.loc[df.median_house_value < df.median_house_value.quantile(0.05),['median_house_value','population']])
# df_min_val = df.loc[df.median_house_value < df.median_house_value.quantile(0.05)]
# print(df_min_val.population.max())