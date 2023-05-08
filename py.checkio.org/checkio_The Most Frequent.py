"""
Дана последовательность строк. Вам нужно определить наиболее часто встречаемую строку в последовательности.
Входные данные: список строк.
Выходные данные: строка.
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
"""

def most_frequent(data) :
    slov = {}
    for i in data:
        if i in slov:
            slov[i] += 1
        else:
            slov[i] = 1
    for i, v in slov.items():
        if v == max(slov.values()):
            return i


data = ["a", "b", "c", "a", "b", "a"]
res = most_frequent(data)
print(res)