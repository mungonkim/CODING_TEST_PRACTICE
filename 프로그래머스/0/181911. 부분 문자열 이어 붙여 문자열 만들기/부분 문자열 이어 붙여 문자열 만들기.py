def solution(my_strings, parts):
    ans = []
    for t, (s, e) in zip(my_strings, parts):
        ans.append(t[s:e+1])
    return ''.join(ans)
