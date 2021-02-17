def solution(s):
    tmp=list(map(int,s.split()))
    maxx=-2167000000
    minn=2167000000
    for i in tmp:
        if i>maxx:
            maxx=i
        if i<minn:
            minn=i
            
    answer = str(minn)+" "+str(maxx)
    return answer