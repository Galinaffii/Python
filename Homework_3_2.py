author = 'Юрий Стрелкин'

'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''
'''
    name = input('enter name')
    surname = input('enter surname')
    year = int(input('enter year'))
    city = input('enter city')
    email = input('enter email')
    phone = input('input phone')
'''
def my_func (name, surname, year, city, email, phone):
     return ' '.join([name, surname, year, city, email, phone])
print(my_func(surname = 'Semenov', name = 'Nikita', year = '1907', city = 'Moscow', email = 'Python@gmail.com', phone = '8-921-555-55-55'))