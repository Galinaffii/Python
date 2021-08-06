author = 'Юрий Стрелкин'

'''
Программа запрашивает у пользователя строку чисел, разделенных 
пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный
символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
'''

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Z for quit - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'z' or number[el] == 'Z':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')
my_sum()