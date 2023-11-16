# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# input_list = "a a a b c a a d c d d"
# user_list = input_list.split()


# result_list = []



# for i in range(len(user_list)):
#         tmp = user_list[:i].count(user_list[i])
#         if tmp >= 1:
#                 result_list.append(f'{user_list[i]}_{tmp}')
#         else:
#                 result_list.append(user_list[i])
#         user_list[:3].count(user_list[i])
# print(result_list)

# print(" ".join(result_list))




# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


# s = "She sells sea shells on the sea shore The shellsthat she sells are sea shells I'm sure. So if she sells seashells on the sea shore I'm sure that the shells are seashore shells" 
# s_list = set(s.lower().strip().split())

# print (len(s_list))
# print(s_list)



# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)

# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n) 


import random
sequence = [random.randint(0,20) for _ in range(10)]
print(sequence)
max_value = 0
found_zero = False

for num in sequence:
        if sequence[0] == 0:
print("0 находится на 1 месте в последовательности, максимального числа до него нет")
found_zero = True
        break
        if num == 0:
        print("Наибольшее значение, завершающееся первым встретившимся нулем:", max_value)
found_zero = True
        break
elif num > max_value:
        max_value = num

        if found_zero == False:
        print("В последовательности нет нуля")