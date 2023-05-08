"""
2194. Cells in a Range on an Excel Sheet
A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:
<col> denotes the column number c of the cell. It is represented by alphabetical letters.
For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
<row> is the row number r of the cell. The rth row is represented by the integer r.
You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents the column c1, <row1>
represents the row r1, <col2> represents the column c2, and <row2> represents the row r2, such that r1 <= r2 and c1 <= c2.
Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2. The cells should be represented as strings
in the format mentioned above and be sorted in non-decreasing order first by columns and then by rows.
"""
import string
def cellsInRange(s):
    all_letters = string.ascii_uppercase
    all_numbers = "123456789"
    l =[]
    first_position, second_position = s.split(":")
    my_words = ""
    for symbol in all_letters:
        if symbol >= first_position[0]:
            if symbol > second_position[0]:
                break
            my_words += symbol
    numbers = all_numbers[int(first_position[1])-1:int(second_position[1])]
    for i in my_words:
        for y in numbers:
            l.append(i+y)
    return sorted(l)




s = "U7:X9"
res = cellsInRange(s)
print(res)