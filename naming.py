"""Задания по стилю кода и именованию переменных."""

# напиши команду, которая проверяет, ссылаются ли
# переменные spam и eggs на один и тот же объект в пямяти
spam = None
eggs = None
id(spam) == id(eggs)

# придумай название для переменной, которая хранит список
# активных студентов, оставь этот список пустым

active_stud = []

# назови переменную, которая хранит текущее количество студентов в потоке

current_stud = []

# придумай две переменных для обозначения самого маленького и самого большого
# числа в диапазоне и запиши в них числа 1 и 45

nano = 1
google = 45

# создай константу для хранения числа Пи и запиши в неё первые 10 знаков

import math
PI_VALUE = ("%.10f" % math.pi)
print(PI_VALUE)
