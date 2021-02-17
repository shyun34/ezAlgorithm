from _collections import deque


def bfs(graph, start, visited):
    # 시작노드가 방문했을경우 유효성 검사
    if visited[start]:
        return 0;

    # 큐 구현을 위해 deque 라이브러리 사용
    que = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while que:
        # 큐에서 하나의 원소를 뽑아 출력
        v = que.popleft()

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True

    return 1


def solution(n, computers):
    answer = 0

    # 입력배열에 따른 그래프 선언
    graph = [[] for _ in range(len(computers) + 1)]

    # 각 노드가 방문된 정보를 리스트 자료형으로 표현
    visited = [False] * (len(computers) + 1)

    # 입력배열을 그래프 형식으로 변환
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if (i == j):
                continue
            elif (computers[i][j] == 1):
                graph[i + 1].append(j + 1)

    # 모든노드를 시작점으로 bfs탐색
    for i in range(1, len(graph)):
        answer += bfs(graph, i, visited)

    print("answer : ",answer)
    return answer

if __name__ == "__main__":
    #출력값
    answer = 0
    #입력값
    computers =[[1,1,0] , [1,1,0] , [0,0,1]]

    solution(3,computers)


