"""You have a text and a list of words. You need to check if the words in a list appear in the same order as in the given text.
Cases you should expect while solving this challenge:
a word from the list is not in the text - your function should return False;
any word can appear more than once in a text - use only the first one;
two words in the given list are the same - your function should return False;
the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
the text includes only English letters and spaces.
Input: Two arguments. The first one is a given text, the second is a list of words.
Output: A bool.
"""
def words_order(text, words):
    l_num =[]
    count = 0
    l_test= text.split()
    for i in words:
        count +=1
        if i in l_test:
            l_num.append(l_test.index(i))
        else:
            return False
    n = 0
    for i in l_num[1:]:
        if l_num[n] >= i:
            return False
        n += 1
    return True



text = "hi world world im here hi world world im here"
words = ["world", "here"]
res = words_order(text, words)
print(res)