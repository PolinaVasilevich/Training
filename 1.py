'''
Напишите декоратор flip, который делает так, что задекорированная функция принимает все свои
неименованные аргументы в порядке, обратном тому,
в котором их передали (для аргументов с именем не вполне правильно
учитывать порядок, в котором они были переданы)
'''


def flip(function):
    def wrapper(*args, **kwargs):
        function(*args[::-1], **kwargs)
    return wrapper


@flip
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res


div(2, 4, show=True)


