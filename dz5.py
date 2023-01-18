import random

txt = "абв"
print(txt)
num_word = (int(input("Количество слов в тексте: ")))
list_word = []
for x in range(num_word):
    random_txt = random.sample(txt, 3)
    list_word.append("".join(random_txt))

print(" ".join(list_word))

list_word2 = list(filter(lambda x: txt not in x, list_word))
print(" ".join(list_word2))
