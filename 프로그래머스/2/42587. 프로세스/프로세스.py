from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque([(v, i) for i, v in enumerate(priorities)])
    
    while queue:
        current = queue.popleft() #처음
        
        if any(current[0] < p[0] for p in queue):
            queue.append(current)
        else:
            answer += 1
            
            if current[1] == location:
                return answer