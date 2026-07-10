from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    queue = deque(truck_weights) #대기 트럭
    bridge = deque([0] * bridge_length) #다리 상황
    
    current_weight = 0 #현재 다리 위에 있는 트럭들의 총 무게
    
    while bridge:
        
        answer += 1
        current_weight -= bridge.popleft()
            
        if queue:
            if current_weight + queue[0] <= weight:
                next_truck = queue.popleft()
                bridge.append(next_truck)
                current_weight += next_truck
            else:
                bridge.append(0)
    
    return answer