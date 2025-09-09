def solution(a, b, c, d):
    dice = [a, b, c, d]

    # 숫자 -> 개수 딕셔너리
    dic = {}
    for x in dice:
        dic[x] = dic.get(x, 0) + 1

    # 패턴 분기: 빈도 멀티셋으로 구분
    freq = sorted(dic.values(), reverse=True)  # [4], [3,1], [2,2], [2,1,1], [1,1,1,1]

    if freq == [4]:
        # 모두 동일
        p, = dic.keys()
        return 1111 * p

    elif freq == [3, 1]:
        # 3+1
        p = next(k for k, v in dic.items() if v == 3)
        q = next(k for k, v in dic.items() if v == 1)
        return (10 * p + q) ** 2

    elif freq == [2, 2]:
        # 2+2
        p, q = [k for k, v in dic.items() if v == 2]
        return (p + q) * abs(p - q)

    elif freq == [2, 1, 1]:
        # 2+1+1  → 한 쌍이 아닌 두 수의 곱
        q, r = [k for k, v in dic.items() if v == 1]
        return q * r

    else:
        # 1+1+1+1
        return min(dice)
