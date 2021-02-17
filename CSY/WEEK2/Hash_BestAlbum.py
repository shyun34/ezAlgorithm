import sys
sys.stdin=open("input.txt","rt")

def solution(genres, plays):
    dic={}
    max_key=""
    play_count=[]
    answer = []
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]]+=plays[i]
        else:
              dic[genres[i]]=plays[i]
    for _ in range(len(dic)):
        maxx=-2167000000
        for key,value in dic.items():
            if value>maxx:
                maxx=value
                max_key=key
        play_count.append(max_key,)
        del dic[max_key]
    tmp=[]
    for key in play_count:
            tmp.clear()
            for i,(g,p) in enumerate(zip(genres,plays)):
                if g==key:
                    tmp.append([p,i])
            tmp.sort(key=lambda x:(x[0],-x[1]))
            if len(tmp)==1:
                answer.append(tmp[0][1])
            else:
                answer.append(tmp[-1][1])
                answer.append(tmp[-2][1])
 
    return answer

if __name__=="__main__":
    print(solution(["classic", "pop", "classic", "classic", "pop","k-pop"],[500, 600, 800, 800, 2500,10]))