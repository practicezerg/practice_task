"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
You are given an array of strings sentences, where each sentences[i] represents a single sentence.
Return the maximum number of words that appear in a single sentence.
"""

def work(sentences):
    l = []
    for i in sentences:
        try1 = i.split(" ")
        l.append(len(try1))
    return max(l)



sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
res = work(sentences)
print(res)