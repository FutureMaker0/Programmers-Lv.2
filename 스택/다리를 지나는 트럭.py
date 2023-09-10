# 큐는 while 반복문 사용

def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    bridge_sum = 0
    
    sec = 0
    while bridge:
        out_truck = bridge.pop(0)
        bridge_sum -= out_truck
        sec += 1
        
        if truck_weights:
            if bridge_sum + truck_weights[0] <= weight:
                
                # 첫 원소를 적용하고나서는 뺴야되기 때문에 pop()을 쓰는게 맞다.
                in_truck = truck_weights.pop(0)
                bridge.append(in_truck)
                
                bridge_sum += in_truck 
                # pop()은 이런데서 변수로 함부로 남용하면 안된다.
                # 답이 달라져버린다, 별도 변수에 값을 담아 활용하자.
                
            else:
                bridge.append(0)
                
    return sec
    
'''
1. 다리 길이만큼의 배열을 하나 만들어준다.
2. 대기하는 트럭이 있다면 트럭의 무게를 싣고, 없으면 0으로 채워준다.
3. 현재 다리 위에 있는 트럭무게 + 바로뒤 대기차 무게의 합이 한계치보다 낮으면 append 해준다.
4. 한계치보다 높으면 앞으로 하나 pop해주고 append(0)으로 길이 및 무게 유지시켜준다.
5. pop(0)를 해서 타겟트럭 또는 모든 트럭이 다 배열을 탈출하는 횟수를 answer로 리턴한다.
'''
