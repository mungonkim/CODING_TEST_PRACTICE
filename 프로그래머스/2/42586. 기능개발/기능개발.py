def solution(progresses, speeds):
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
    
    return cnt