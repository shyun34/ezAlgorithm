import sys
from collections import deque
sys.stdin = open("input.txt","rt")
 
def solution(bridge_length, weight, truck_weights):
    answer=0
    q=[0]*bridge_length #다리를 미리 구현해놓는다.

    
    while q:
        answer+=1
        q.pop(0) #pop(0) 첫번째 원소가 pop 된다. deque로 구현 안해도 됨.
        if truck_weights: #대기중인 트럭이 있는 경우 append 된다.
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)

    return answer



if __name__ == "__main__":
    print(solution(100, 100, [10]))
    

    
