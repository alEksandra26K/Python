with open('text_words.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст: '))
with open('text_words.txt', 'r') as file:
    my_txt = file.readline()
    txt_1 = my_txt.split()

print(my_txt)

def file_encod(txt):
    encond = ''
    pr_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != pr_char:
            if pr_char:
                encond += str(count) + pr_char
            count = 1
            pr_char = char
        else:
            count += 1
    else:
        encond += str(count) + pr_char
        return encond


txt_1 = file_encod(my_txt)

with open('text_code_words.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_1}')
print(txt_1)

