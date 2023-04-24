"""
A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'),
punctuation marks ('!', '.', and ','), and spaces (' ') only.
Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.
A token is a valid word if all three of the following are true:
It only contains lowercase letters, hyphens, and/or punctuation (no digits).
There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters
("a-b" is valid, but "-ab" and "ab-" are not valid).
There is at most one punctuation mark.
If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".
Given a string sentence, return the number of valid words in sentence.
"""
import re


def work(sentence):
    l = sentence.split()
    l_res = []
    pattern_one = f'^([a-z]+(-?[a-z]+)?)?(!|\.|,)?$'
    for i in l:
        test = re.match(pattern_one, i)
        if test != None:
            l_res.append(test[0])
    return len(l_res)



sentence = "-"
# sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener. test2  12ddd, 114sad123asd-! Time -ab ab- a-b cd! cd,. a!b c,. ! a!"
# sentence = "f    6c x2"
# sentence = "2j.df0e"
# sentence = "alice and  bob are playing stone-game10"
# sentence = "!this  1-s b8d!"
res = work(sentence)
print(res)
