"""
You are given the strings key and message, which represent a cipher key and a secret message, respectively.
The steps to decode message are as follows:
Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet),
we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message."""

def decodeMessage(key, message):
    key = key.replace(" ", "")
    key_res = ""
    for i in key:
        if i not in key_res:
            key_res += i
    string = "abcdefghijklmnopqrstuvwxyz"
    n = 0
    form = {}
    for i in key_res:
        form[i] = string[n]
        n += 1
    result = ""
    for i in message:
        if i == " ":
            result += i
        else:
            result += form[i]
    return result





key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
res = decodeMessage(key, message)
print(res)
