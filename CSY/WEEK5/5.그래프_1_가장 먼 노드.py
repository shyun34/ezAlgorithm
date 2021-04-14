import sys
from collections import deque
sys.stdin = open("input.txt","rt")
#4:08 ~ 4:25



def solution(n, edge):
    answer = 0
    #방문했는지 안했는지 체크
    visited = [-1] * (n+1)
    #인접노드 생성
    adj = [[] for _ in range(n+1)]
    for i in edge:
        x=i[0]
        y=i[1]
        adj[x].append(y)
        adj[y].append(x)
    print(adj)

    def BFS(val,visited,adj):
        cnt=0
        q=deque([[val,cnt]])
        while q:
            # 인접노드 탐색
            value = q.popleft()
            print(value,sep='\n')
            v = value[0]
            c = value[1]
            if visited[v]==-1: # 아직 방문 한적 없다면
                visited[v]=cnt
                cnt+=1
                for i in adj[v]:
                    q.append([i,cnt])
                print(q)
       
    BFS(1,visited,adj)

    return answer


if __name__ == "__main__":
    print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))