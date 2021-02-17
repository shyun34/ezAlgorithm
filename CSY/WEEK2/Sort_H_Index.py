def solution(citations):
    maxx=len(citations)
    answer = 0
    for i in range(maxx,0,-1):
        up=0
        down=0
        for j in citations:
            if j>=i:
                up+=1
            else:
                down+=1
        if i<=up and i>=down:
            answer=i
            break

    return answer

if __name__=="__main__":
    print(solution([0, 1, 2]))