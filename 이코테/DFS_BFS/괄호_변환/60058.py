def seperate(p):
    u, v = '', ''
    cnt = [0, 0]
    for i in range(len(p)):
        if p[i] == '(':
            cnt[0] += 1
        else:
            cnt[1] += 1

        if cnt[0] == cnt[1]:
            u = p[:i + 1]
            v = p[i + 1:]
            break
    return u, v


def is_right(p):
    stack = 0
    for i in range(len(p)):
        if p[i] == '(':
            stack += 1
        else:
            if stack:
                stack -= 1
            else:
                return False
    return True


def p_flip(p):
    new_p = ''
    for i in range(len(p)):
        if p[i] == '(':
            new_p += ')'
        else:
            new_p += '('
    return new_p


def solution(p):  # p 균형잡힌 괄호 문자열(왼쪽 괄호, 오른쪽 괄호의 개수 일치)
    # 1. 빈 문자열인 경우, 빈 문자열을 반환
    if p:
        # 2. 문자열 w를 균형잡힌 괄호 문자열 u, v로 분리
        u, v = seperate(p)

        # 3. u가 올바른 문자열이 맞는지 판단
        if is_right(u):
            return u + solution(v)
        else:
            # 4.1
            new_p = '('

            # 4.2
            new_p += solution(v)

            # 4.3
            new_p += ')'

            # 4.4
            new_p += p_flip(u[1:-1])

            return new_p
    else:
        return ''