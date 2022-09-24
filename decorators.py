import datetime
import os
import pathlib


def Logator(some_function):
    def getpath():
        path = pathlib.Path.cwd()
        return path

    def new_function(*args, **kwargs):
        os.chdir(getpath())
        log = []
        dt = datetime.datetime.now()
        dt_string = dt.strftime("%d/%m/%Y %H:%M:%S")
        log.append(dt_string)
        log.append(f'Вызвана функция "{some_function.__name__}"')
        log.append(f'{args} / {kwargs}')
        result = some_function(*args, **kwargs)
        log.append(f'Результат работы функции: \n {result}')
        with open('log.txt', 'a+', encoding='UTF-8') as file:
            for irems in log:
                file.write(irems + '\n')
        return result
    return new_function