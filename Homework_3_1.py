author = 'Юрий Стрелкин'

'''
Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
'''

def div(*args):
    try:
        num_1 = int(input("Input dividend "))
        num_2 = int(input("Input divider "))
        res = num_1 / num_2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Wrong! You can't use 0 as a devider"
    return res
    '''
    if arg2 != 0:
        return num_1 / num_2
    else:
        print("Wrong! Devider can't be 0")
    '''
print(f'result  {div()}')