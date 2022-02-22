import sys
sys.stdin = open('1181_input.txt', 'r')

N = int(input())
words = [input() for i in range(N)]
words.sort(key=lambda x: (len(x), x))
i = 1
while i < len(words):
    if words[i-1] == words[i]:
        words.pop(i)
    else:
        i += 1
for word in words:
    print(word)