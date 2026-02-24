import sys
input = sys.stdin.readline

n = int(input())

length = 0
digit = 1  #현재 자리 수 
start = 1  # 현재 자리수에서의 시작 숫자 (1, 10, 100 ...)

while True:
    end = start * 10 -1
    
    if n <= end:
        length += (n - start + 1) * digit
        break
    
    length += (end - start +1) * digit
    
    digit += 1
    start *= 10

print(length)