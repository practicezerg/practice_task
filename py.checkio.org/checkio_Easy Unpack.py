"""Ваша цель сейчас — создать функцию, которая принимает на вход кортеж и возвращает кортеж из 3 элементов: первого,
 третьего и второго с конца элементов заданного кортежа."""
def easy_unpack(elements):
    res = []
    res.append(elements[0])
    res.append(elements[2])
    res.append(elements[-2])
    return tuple(res)


elements = (1, 2, 3, 4, 5, 6, 7, 9)
res = easy_unpack(elements)
print(res)