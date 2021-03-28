import sys
from collections import deque
sys.stdin = open("input.txt","rt")
 

def solution(n, lost, reserve):
    ch_lost=[1]*len(lost) #체육복을 잃어버린 학생
    ch_reserve=[0]*(len(reserve)) #여분의 체육복이 있는 학생
    
    #체육복을 잃어버렸지만 본인이 여분이 있으면 체크
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i]==reserve[j] and ch_reserve[j]==0:
                ch_reserve[j]=1
                ch_lost[i]=0
                break

    #체육복을 잃어버렸지만 본인이 여분이 없는 경우 빌려주는 경우 체크
    for i in range(len(lost)):
        if ch_lost[i]==1:
             for j in range(len(reserve)):
                    if (reserve[j]==lost[i]-1 or reserve[j]==lost[i]+1) and ch_reserve[j]==0 :
                            ch_lost[i]=0
                            ch_reserve[j]=1
    #ch_lost에는 체육복을 빌리지 못한 학생들이 1로 되어있다.
    return n - sum(ch_lost)

if __name__ == "__main__":
    print(solution(5,[2,3,4],[1,2,3]))
    

    
