#큐를 이용한 풀이
import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    
    days_queue = deque([math.ceil((100-p) / s) for p, s in zip(progresses, speeds)])
    
    while days_queue:
        deploy_day = days_queue.popleft()
        cnt = 1
        
        while days_queue and days_queue[0] <= deploy_day:
            days_queue.popleft()
            cnt += 1
        
        answer.append(cnt)
    return answer


#수학적 풀이 
'''def solution(progresses, speeds):
    answer = []
    cnt = 1
    task_1 = test_cnt(progresses[0], speeds[0])
    
    for i in range(1, len(progresses)):
        task_2 = test_cnt(progresses[i], speeds[i])
        if task_1 < task_2:
            answer.append(cnt)
            cnt = 1
            task_1 = task_2
        else:
            cnt += 1
    answer.append(cnt)
    return answer

def test_cnt(p, s):
    cnt = 0
    while p < 100:
        p += s
        cnt += 1
    
    return cnt '''
