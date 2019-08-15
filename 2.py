'''
Напишите декоратор introduce_on_debug, который делает так,
что задекорированная функция печатает своё имя при вызове в
стандартный поток вывода ("представляется"), но только если
встроенная константа __debug__ имеет значение
True (то есть если программа не запущена с флажком оптимизации -o).

Чтобы было проще всё это проверять, используйте в теле декоратора вместо
встроенной константы __debug__ просто переменную debug (её значение будет установлено за вас).

Версию с честным __debug__ вместо debug можете протестировать, запустив у себя программу с флажком -ο и без него
'''


def introduce_on_debug(function):
    def wrapper(*args, **kwargs):
        if __debug__:
            print(function.__name__)
            function(*args, **kwargs)
    return wrapper


@introduce_on_debug
def simple_function(x):
    print(x)


print(simple_function(1234))
