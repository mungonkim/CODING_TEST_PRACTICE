def y_fee(call):
    m = 0
    for i in call:
        m += 10 + 10*(i//30)
    return m

def m_fee(call):
    m = 0
    for i in call:
        m += 15 + 15*(i//60)
    return m

n = int(input())
call = list(map(int, input().split()))

if y_fee(call) < m_fee(call):
    print('Y', y_fee(call))
elif m_fee(call) < y_fee(call):
    print('M', m_fee(call))
else:
    print('Y', 'M', y_fee(call))
