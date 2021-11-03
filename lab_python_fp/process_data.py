import json
import sys
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1
from lab_python_fp.gen_random import gen_random
path = '/home/ilya/InternetAppDevelopment/data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path) as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк


@print_result
def f1(arg):
    return list(sorted((set(x['job-name'].casefold() for x in arg))))


@print_result
def f2(arg):

    return list(filter(lambda prof_str: prof_str.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda prof_str: prof_str + ' с опытом Python', arg))


@print_result
def f4(arg):
    return list(prof_name + ', зарплата ' + str(salary) + ' руб.' for prof_name, salary in
                zip(arg,  gen_random(len(arg), 100000, 200000)))


if __name__ == '__main__':
    with cm_timer_1('json processing'):
        f4(f3(f2(f1(data))))
