def solution(s):
    answer = True
    cnt = []
    for i in s:
        if i == ')':
            if not cnt:
                return False
            else:
                cnt.pop()
        else:
            cnt.append(i)
    if cnt:
        return False
    return True