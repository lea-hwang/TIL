import sys
sys.stdin = open("input.txt")

word = input()

def check(word):
    while word:
        for i in range(1, 13):
            if len(word) < 4*i:
                return 0
            if word[0:4*i] == 'w' * i + 'o' * i + 'l' * i + 'f' * i:
                word = word[4*i:]
                break
        else:
            return 0
    return 1

print(check(word))
