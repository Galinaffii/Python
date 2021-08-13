author = 'Юрий Стрелкин'

'''
Создать текстовый файл (не программно), сохранить
в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

my_file = open('Lesson_5_2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('Lesson_5_2.txt', 'r')
content = my_file.readlines()
print(f'Строк в файле - {len(content)}')
my_file = open('Lesson_5_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('Lesson_5_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Количество слов - {len(content)}')
my_file.close()
