def solution(citations):
    citations.sort()
    for i, pp in enumerate(citations):
        if pp >= len(citations)-i:
            return len(citations)-i
    answer = 0
    return answer