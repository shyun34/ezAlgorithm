import sys
from collections import Counter
sys.stdin = open("input.txt","rt")
#4:08 ~ 4:25



def solution(m, n, puddles):
    answer = [[0]*(m+1) for _ in range(n+1)]
    answer[1][1]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i==1 and j==1:
                continue
            if [j,i] in puddles:
                answer[j][i]=0
            else:
                answer[j][i]=answer[j-1][i]+answer[j][i-1]

    return answer[n][m]%1000000007


if __name__ == "__main__":
    print(solution(4,3,[[2,2]]))