"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:"""
def abbrev_name(name):
    res = name.split()
    return (res[0][0]).capitalize() +  "." + (res[1][0]).capitalize()

name = "sam Harris"
res = abbrev_name(name)
print(res)