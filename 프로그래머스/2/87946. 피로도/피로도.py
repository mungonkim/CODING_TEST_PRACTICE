from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    
    for p in permutations(dungeons):
        current_k = k
        count = 0
        
        for min_req, cost in p:
            if current_k >= min_req:
                current_k -= cost
                count += 1
            else:
                break
        
        max_count = max(max_count, count)
    return max_count