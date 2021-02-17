import sys
from collections import deque
sys.stdin=open("input.txt","rt")

def solution(genres, plays):
    dic={}
    play_count=[]
    answer = []

    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i],0) + plays[i]

    for i in range(len(genres)):
        play_count.append([genres[i], plays[i], i])
    dic = sorted(dic.items(),key=lambda dic:dic[1],reverse=True)
    play_count=sorted(play_count,key=lambda x:(-x[1],x[2]))
    tmp=[]
    for k in dic:
            tmp.clear()
            for i in play_count:
                if i[0]==k[0]:
                    tmp.append([i[0],i[2]])
            if len(tmp)==1:
                answer.append(tmp[0][1])
            else:
                answer.append(tmp[0][1])
                answer.append(tmp[1][1])
 
    return answer

if __name__=="__main__":
    print(solution(["classic", "pop", "classic", "classic", "pop","k-pop"],[500, 600, 800, 800, 2500,10]))