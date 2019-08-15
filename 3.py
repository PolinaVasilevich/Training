'''
Напишите декоратор optional_introduce, который делает так,
что у задекорированной функции появляется дополнительный параметр introduce
со значением False по умолчанию (именованный параметр), причём если функция вызвана с introduce=True,
то она перед возвращением результата напечатает своё имя в стандартный поток вывода ("представится"),
а если с introduce=False или без явного указания introduce вовсе, то она просто вернёт результат.

Мы предполагаем, что у исходной функции параметра с именем introduce не было.
'''

def optional_introduce(function):
    def wrapper(*args, introduce=False, **kwargs):
        if introduce:
            print('Function name: {}'.format(function.__name__))
        function(*args, introduce=False, **kwargs)
    return wrapper


@optional_introduce
def simple_func(*args, **kwargs):
    print('Result: {} and {}'.format(args, kwargs))


simple_func(introduce=True)

