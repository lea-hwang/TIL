s = "abcabcabcabcdedededede"
N = len(s)

min_val = N
for l in range(1, N):
    result = ""
    idx = 0
    cur = ""
    cnt = 1
    while idx < N:
        if cur != s[idx:idx+l]:
            if cnt > 1:
                result += str(cnt)
            result += cur
            cur = s[idx:idx+l]
            cnt = 1
        else:
            cnt += 1
        idx += l
    if cnt != 1:
        result += str(cnt)
    result += cur
    min_val = min(min_val, len(result))
print(min_val)