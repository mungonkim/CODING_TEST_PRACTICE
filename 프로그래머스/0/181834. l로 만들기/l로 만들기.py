def solution(myString):
    arr = list(myString)
    for i in range(len(arr)):
        if arr[i] < 'l':
            arr[i] = 'l'
    return "".join(arr)
