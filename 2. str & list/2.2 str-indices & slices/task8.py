word1, word2 = input().split()

print(word1[:len(word2)][1::2] == word2[1::2])

