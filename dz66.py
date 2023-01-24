
# 1


# result_list = []
# list = [int(i) for i in input("Введите список чисел: ").split()]
# for i in range(1, len(list)):
#     if list[i] > list[i-1]:
#         (result_list.append(list[i]))
# print("Исходный список: ", list)
# print("Список, элементы которого больше предыдущего: ", result_list)

# 2
n = int(input("Введите размер списка от 20: "))
spam = list(range(20, n+1))
print(spam)
print([el for el in range(20, n+1) if el % 20 == 0 or el % 21 == 0])

# 3
# def thesaurus(*names):
#     res = {}
#     for name in names:
#         key = name[0].capitalize()
#         if key not in res:
#             res[key] = []
#         res[key].append(name)
#     return res

# print(thesaurus("Иван", "Мария", "Петр", "Илья"))

