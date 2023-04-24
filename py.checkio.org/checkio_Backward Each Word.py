"""
Требуется обратить порядок букв в каждом слове предоставленной строки, так чтобы слова остались на своих местах.
Входные данные: строка.
Выходные данные: строка.
"""
def backward_string_by_word(text):
    l_res = []
    if " " in text:
        l = text.split(" ")
    else:
        return text[::-1]
    for i in l:
        l_res.append(i[::-1])
    return " ".join(l_res)
text = "hello  world"
res = backward_string_by_word(text)
print(res)