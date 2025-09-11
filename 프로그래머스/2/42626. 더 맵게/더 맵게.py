import heapq

def solution(scoville, K):
    heapq.heapify(scoville)

    if scoville[0] >= K:   
        return 0

    answer = 0
    while len(scoville) >= 2 and scoville[0] < K:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        mixed = a + (b * 2)
        heapq.heappush(scoville, mixed)
        answer += 1

    return answer if scoville and scoville[0] >= K else -1
