"""В данном списке первый элемент должен стать последним.
Пустой список или список из одного элемента не должен измениться."""

def replace_first(items):
    if len(items) > 0:
        trust = items.pop(0)
        items.append(trust)
        return items
    else:
        return items

items = [1, 2, 3, 4]
res = replace_first(items)
print(res)