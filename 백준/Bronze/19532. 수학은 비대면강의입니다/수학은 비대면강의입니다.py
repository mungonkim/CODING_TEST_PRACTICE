# 크래머 공식 이용 (유일해 ⇒ a*e - b*d != 0)

a, b, c, d, e, f = map(int, input().split())

det = a*e - b*d               
x = (c*e - b*f) // det        
y = (a*f - c*d) // det

print(x, y)
