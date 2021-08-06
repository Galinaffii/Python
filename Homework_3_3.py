author = 'Юрий Стрелкин'

'''
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
'''
def my_func(num_1 , num_2, num_3):
    if num_1 >= num_3 and num_2 >= num_3:
        return num_1 + num_2
    elif num_1 > num_2 and num_1 < num_3:
        return num_1 + num_3
    else:
        return num_2 + num_3
print(f'Result - {my_func(int(input("enter first argument ")), int(input("enter second argument ")), int(input("enter third argument ")))}')