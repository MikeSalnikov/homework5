# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open("file_to_4.txt", "r", encoding='utf-8') as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(dict[i[0]] + '  ' + i[1])
with open('file_to_4_new.txt', 'w+', encoding='utf-8') as f2:
    f2.writelines(new_file)
    f2.seek(0)
    cont2 = f2.read()
    print(cont2)