# // 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다.
# // 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 
# // 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 
# // 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

# // 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 
# // 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

# // 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# // 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# // i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# // computer[i][i]는 항상 1입니다.


# 깊이우선탐색  
def dfs(computers, start, explored):
   
    print('start', start)
    print('explored', explored)

    if start in explored:   # 탐색했으면 빠져나옴
        return 0, explored    
    
    explored.add(start)  #안 탐색했으면 탐색란에 더함

    neighbors = computers[start]   #옆 노드

    for ni in range(len(neighbors)):    #옆노드에서 다시 탐색
        

        ###############################
        
        if ni == start or neighbors[ni] == 0: continue  # 0(이어지지않음) or 자기자신 이면 그냥넘김
        
        ###############################


        if ni not in explored:  # 탐색하지않았으면 다시 재귀탐색
            dfs(computers, ni, explored)    

    return 1, explored  # 모두 돌았을 경우 1과 탐색리스트 리턴



def solution(n, computers):
   
    answer = 0  # 구하려는 네트워크 노드의 수
    explored = set()  #탐색한 리스트 모음
    
    for start in range(0, n):   # 0부터 n만큼 반복
       
        res, explored = dfs(computers, start, explored)
      
        answer += res
    
    return answer


solution(6, [[1, 0, 1, 1, 0, 0], 
[0, 1, 0, 0, 1, 1],
[1, 0, 1, 1, 1, 1] ,
[1, 0, 1, 1, 1, 1] ,
[0, 1, 1, 1, 1, 1] ,
[0, 1, 1, 1, 1, 1]
]) #2
# solution(4, [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 0], [1, 1, 0, 1]]); #2
# solution(4, [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]); #2
