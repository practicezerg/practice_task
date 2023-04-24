"""You need to count how many non-empty lines a given text has.
An empty line is a line without symbols or the one that contains only spaces.
Input: A text.
Output: An int.
"""
def non_empty_lines(text):
    count = 0
    if "\n" in text:
        l = text.split("\n")
    if len(text) == 0:
        return 0
    for i in l:
        for char in i:
            if char.isdigit() or char.isalpha():
                count += 1
                break
    return count

text = "\nonly one line\n            "
res = non_empty_lines(text)
print(res)