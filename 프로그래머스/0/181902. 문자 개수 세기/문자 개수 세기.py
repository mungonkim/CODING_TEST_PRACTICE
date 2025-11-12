def solution(my_string):
    result = [0] * 52  

    for ch in my_string:
        if 'A' <= ch <= 'Z':
            result[ord(ch) - ord('A')] += 1
        elif 'a' <= ch <= 'z':
            result[26 + (ord(ch) - ord('a'))] += 1

    return result
