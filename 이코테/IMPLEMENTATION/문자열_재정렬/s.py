import sys
sys.stdin = open('input.txt', 'r')

line = input()

letter = [0] * 26
total = 0
for l in line:
    if l.isalpha():
        letter[ord(l) - 65] += 1
    else:
        total += int(l)

for i in range(26):
    print(chr(65+i) * letter[i], end="")
print(total)