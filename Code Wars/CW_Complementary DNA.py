"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the
 development and functioning of living organisms.
If you want to know more: http://en.wikipedia.org/wiki/DNA
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of
 the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or
  there is no DNA at all (again, except for Haskell).
More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)
A => T
T => A
C => G
G => C
"""
def DNA_strand(dna):
    res = ""
    for symbol in dna:
        if symbol == "A":
            symbol = "T"
        elif symbol == "T":
            symbol = "A"
        elif symbol == "C":
            symbol = "G"
        elif symbol == "G":
            symbol = "C"
        res = res + symbol
    return res

dna = "ATTGC"
res = DNA_strand(dna)
print(res)