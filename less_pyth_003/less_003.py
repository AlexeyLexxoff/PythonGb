# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


# list_num = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list_num)))

# from random import randint

# list_num = [1, 1, 2, 0, -1, 3, 4, 4, 4, 487]
# count = 0
# new_list = []
# for i in list_num:
#     if i not in new_list:
#         new_list.append(i)
# print(len(new_list))
# print(new_list)



# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# list_num = [1, 2, 3, 4, 5]
# k = 3
# # print(list_num)
# # for i in range(k):
# #     list_num.insert(0, list_num.pop())
# # print(list_num)



# list_num = [1, 2, 3, 4, 5]
# k = 3
# print(list_num[:k])
# print(list_num[k:])

# result_list =  list_num[k:-1] + list_num[0:k]
# print(result_list)



# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводи

# user_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# result_set = set()

# for el in user_list:
#     result_set.add(el.values())

# print(result_set)

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# user_num = [0, -1, 5, 2, 3]
# count = 0
# for i in range(len(user_num)-1):
#     if user_num[i] < user_num[i + 1]:
#         count += 1
# print(count)


# user_num = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(user_num)):
#     if user_num[i] < user_num[i - 1]:
#         count += 1
# print(count)