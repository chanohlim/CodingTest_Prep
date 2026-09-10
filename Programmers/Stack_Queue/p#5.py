from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time = 0
    cnt = 0
    bridge_weight = 0
    
    bridge = deque([0] * (bridge_length))
    trucks = deque(truck_weights)
    
    while trucks:
        
        next = trucks[0]
            
        bridge_weight -= bridge.popleft()
        if bridge_weight + next <= weight:
            
            bridge.append(next)
            bridge_weight += next
            trucks.popleft()
            
        else:
            bridge.append(0)
            
        time += 1
        
    time += bridge_length
    
    return time