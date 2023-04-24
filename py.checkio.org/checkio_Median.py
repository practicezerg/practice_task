"""
Медиана — это числовое значение, которое делит сортированый массив чисел на нижнюю и верхнюю половины.
В сортированом массиве с нечётным числом элементов медиана — это число в середине массива. Для массива с чётным числом
элементов, где нет одного элемента точно посередине, медиана — это среднее значение двух чисел, находящихся в середине
 массива. В этой задаче дан непустой массив натуральных чисел. Вам необходимо найти медиану данного массива.
Если ты хочешь больше попрактиковаться с подобным заданием, попробуй миссию Middle Characters.
Входные данные: Массив как список (list) чисел (int).
Выходные данные: Медиана как число (int, float).
"""
def checkio(data):
    data = sorted(data)
    if len(data)%2 == 0:
        return (data[int(len(data)/2)] + data[int((len(data)/2)-1)])/2
    else:
        num = len(data)/2 + 0.5
        return data[int(num)-1]


data = [3, 6, 20, 99, 10, 15]
res = checkio(data)
print(res)