# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("file_to_3.txt", "rt", encoding='utf-8') as f:
    cont = f.readlines()
    f.seek(0)
    sal = []
    for i in range(len(cont)):
        line = f.readline()
        words = line.split()
        if float(words[1]) < 20000:
            print(words[0])
        sal.append(words[1])
    print(f'средний доход сотрудников: {sum(map(float, sal)) / len(sal)}')