# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("file_to_2.txt", "r") as f:
    cont = f.read()
    print(f'содержимое файла: \n{cont}')
    f.seek(0)
    lines = f.readlines()
    print(f'количество строк: {len(lines)}')
    f.seek(0)
    for i in range(len(lines)):
        line = f.readline()
        words = line.split()
        print(f'количество слов в {i + 1}-ой строке: {len(words)}')