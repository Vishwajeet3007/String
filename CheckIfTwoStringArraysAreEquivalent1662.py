def arrayStringAreEqual(word1,word2):
    return "".join(word1) == "".join(word2)
word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(arrayStringAreEqual(word1,word2))
word1 = ["a", "cb"]
word2 = ["ab", "c"]
print(arrayStringAreEqual(word1,word2))
word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]
print(arrayStringAreEqual(word1,word2))