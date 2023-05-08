"""
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram,
or false otherwise.
"""
import string
def checkIfPangram(sentence):
    s = ""
    full_s = string.ascii_lowercase
    for i in full_s:
        if i not in sentence:
            return False
    return True




sentence = "thequickbrownfoxjumpsoverthelazydog"
res = checkIfPangram(sentence)
print(res)