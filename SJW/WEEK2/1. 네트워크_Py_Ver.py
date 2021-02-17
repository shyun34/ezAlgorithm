def dfs(computers, start, explored):
    print('start', start)
    print('explored', explored)
    if start in explored:
        return 0, explored
    explored.add(start)
    neighbors = computers[start]
    for ni in range(len(neighbors)):
        if ni == start or neighbors[ni] == 0: continue
        if ni not in explored:
            dfs(computers, ni, explored)
    return 1, explored

def solution(n, computers):
    answer = 0
    explored = set()
    for start in range(0, n):
        res, explored = dfs(computers, start, explored)
      
        answer += res
    return answer


solution(5, [[1, 1, 0, 0, 1], [1, 1, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 1, 1, 1]])
