"""В этой миссии Вам надо определить, все ли элементы массива равны."""

def all_the_same(elements):
    for i in elements:
        if i != elements[0]:
            return False
    return True

elements = ["a", "a", "a"]
res = all_the_same(elements)
print(res)