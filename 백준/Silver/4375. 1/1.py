while True:
    try:
        n = int(input().strip())
    except:
        break

    length = 1
    res = 1 % n
    while res != 0:
        res = (res * 10 + 1) % n
        length += 1

    print(length)