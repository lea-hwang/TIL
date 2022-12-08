import sys
sys.stdin = open("input.txt")

sentence = input()

# 1. 띄어쓰기로 나누기
# 2. -으로 나누기
sentence = sentence.replace('-', ' ')
sentence = sentence.split(' ')

count = len(sentence)
for i, word in enumerate(sentence):
    for j, letter in enumerate(word):
        if letter == "'":
            if word[:j+1] in ["c'", "j'", "n'", "m'", "t'", "s'", "l'", "d'", "qu'"] and word[j+1] in 'aeiouh':
                count += 1
print(count)