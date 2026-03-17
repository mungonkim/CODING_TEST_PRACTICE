import sys
input = sys.stdin.readline

while True:
    ch = input().rstrip()
    if ch == '0':
        break
    flag = 1
    
    for i in range(len(ch)//2):
        if ch[i] != ch[len(ch)-1-i]:
            flag = 0
            break
    
    if flag == 1:
        print('yes')
    else:
        print('no')