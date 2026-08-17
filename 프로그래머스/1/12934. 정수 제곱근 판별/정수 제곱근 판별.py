import math

def solution(n):
    root = int(math.sqrt(n))
    if root * root == n:
        return (root+1) * (root+1)
    return -1
