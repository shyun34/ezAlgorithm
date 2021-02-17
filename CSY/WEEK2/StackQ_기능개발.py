from collections import deque

def solution(progresses, speeds):
    answer = []
    p=deque(progresses)
    ps=deque(speeds)
    cnt=0
    while p:
        if p[0]>=100:
            p.popleft()
            ps.popleft()
            cnt+=1
        else:
            if cnt>0:
                answer.append(cnt)
                cnt=0
            for i in range(len(p)):
                p[i]+=ps[i]
        if len(p)==0:
            answer.append(cnt)

    return answer