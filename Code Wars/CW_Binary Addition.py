"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before,
or after the addition.
The binary number returned should be a string.
Examples:(Input1, Input2 --> Output (explanation)))
"""

def add_binary(a,b):
    return (bin(a+b)).replace("0b", "")


a, b = 5, 9
res = add_binary(a,b)
print(res)
