from collections import Counter

def solution(topping):
    answer = 0
    brother_map = Counter(topping)
    chul = set()
    
    for t in topping:
        chul.add(t)
        
        brother_map[t] -= 1
        if brother_map[t] == 0:
            del brother_map[t]
            
        if len(brother_map) == len(chul):
            answer += 1
            
    return answer