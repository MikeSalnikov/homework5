#Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

import re
subj = {}
with open('file_to_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        subject, lecture, practise, lab = line.split()
        lecture1 = re.sub(r'-', '0', lecture)
        practise1 = re.sub(r'-', '0', practise)
        lab1 = re.sub(r'-', '0', lab)
        lecture2 = int(re.sub(r'[а-я-()]', '', lecture1))
        practise2 = int(re.sub(r'[а-я-()]', '', practise1))
        lab2 = int(re.sub(r'[а-я-()]', '', lab1))
        subject1 = re.sub(r':', '', subject)
        subj[subject1] = (lecture2) + (practise2) + (lab2)
    print(f'Общее количество часов по предметам - \n{subj}')