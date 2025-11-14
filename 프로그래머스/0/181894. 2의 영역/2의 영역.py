def solution(arr):
    rl = []
    for i in range(len(arr)):
        if arr[i] == 2:
            rl.append(i)
    if rl:
        a, b = min(rl), max(rl)
        return arr[a:b+1]
    else:
        return [-1]
   