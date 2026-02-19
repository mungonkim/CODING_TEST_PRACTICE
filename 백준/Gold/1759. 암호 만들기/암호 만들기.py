L, C = map(int, input().split())
chars = input().split()
chars.sort()

vowels = {'a', 'e', 'i', 'o', 'u'}
result = []

def dfs(start, depth, vowel_cnt, cons_cnt):
    if depth == L:
        if vowel_cnt >= 1 and cons_cnt >= 2:
            print("".join(result))
        return

    for i in range(start, C):
        ch = chars[i]
        result.append(ch)
        if ch in vowels:
            dfs(i + 1, depth + 1, vowel_cnt + 1, cons_cnt)
        else:
            dfs(i + 1, depth + 1, vowel_cnt, cons_cnt + 1)
        result.pop()

dfs(0, 0, 0, 0)
