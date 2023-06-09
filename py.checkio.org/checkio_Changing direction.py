"""
Дан список состоящий из целых чисел. Ваша задача выяснить сколько раз в нем меняется направление при переходе от одного
числа к другому. Если числа равны, то направление не меняется. В случае, если следующий элемент отличается от
предыдущего - необходимо определить в какую сторону поменялось направление.
Давайте взглянем на схему:
На ней изображено следующее:
для фрагмента 1, 2, 2 - направление идет вверх;
для фрагмента 2, 1 - идет вниз;
для фрагмента 1, 2, 2 - снова возрастает.
Так что в данном примере есть всего две точки смены направления: #1 - направление меняется с возрастающего на убывающее,
и #2 - наоборот, начинает опять расти вверх.
Входные данные: Список целых чисел.
Выходные данные: Целое число.
"""
def changing_direction(elements):
    c = 0
    s = ""
    for num in elements[1:]:
        if num > elements[c]:
            s += "u"
        elif num == elements[c]:
            s += ""
        else:
            s += "d"
        c += 1
    print(s)
    return s.count("du") + s.count("ud")


elements = [1, 2, 2, 1, 2, 2]
res = changing_direction(elements)
print(res)


