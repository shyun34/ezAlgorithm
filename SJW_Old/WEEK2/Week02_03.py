from collections import deque
import math


def solution(progresses, speeds):
    # output
    answer = []

    que = deque()

    # 작업시간 연산
    for i in range(len(progresses)):
        que.append(math.ceil((100 - progresses[i]) / speeds[i]))

    # 순서에 따른 작업시간 큰 값 선언
    flag = 0
    # 기능 값 선언
    temp = 0
    while que:
        pop = que.popleft()
        if flag == 0:
            flag = pop
            temp = 1
        # 앞선 큰 작업시간 보다 다음 작업시간이 큰 경우 : 배포 및 기능 초기화
        elif flag < pop:
            flag = pop
            answer.append(temp)
            temp = 1
        # 앞선 큰 작업시간 보다 다음 작업시간이 작은 경우 : 함께 배포될 기능 추가
        else:
            temp += 1

    answer.append(temp)

    print("answer : ",answer)
    return answer


if __name__ == "__main__":
    #input
    progresses = [95,90,99,99,80,99]
    speeds = [1,1,1,1,1,1]

    solution(progresses,speeds)