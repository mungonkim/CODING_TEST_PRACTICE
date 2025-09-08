def solution(l, r):
    start = ((l + 4) // 5) * 5
    answer = [i for i in range(start, r+1, 5) if set(str(i)) <= {'0','5'}]
    return answer if answer else [-1]
