import sys

input = sys.stdin.readline

ch1 = input().strip()
ch2 = input().strip()
ch3 = input().strip()

result = 0

if ch1.isdigit():
    result = int(ch1) + 3
elif ch2.isdigit():
    result = int(ch2) + 2
elif ch3.isdigit():
    result = int(ch3) + 1

if result % 3 == 0 and result % 5 == 0:
    print('FizzBuzz')
elif result % 3 == 0:
    print('Fizz')
elif result % 5 == 0:
    print('Buzz')
else:
    print(result)