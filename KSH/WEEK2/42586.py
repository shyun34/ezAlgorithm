def solution(progresses, speeds):
    days = []
    answer = []
    for i, task in enumerate(progresses):
        took = (100-task)//speeds[i]
        if (100-task)%speeds[i] !=0:
            took=took+1
            
        days.append(took)
    cnt=0
    mx=0
    for i, done in enumerate(days):
        if i==0:
            cnt+=1
            mx=done
        elif done < mx:
            cnt+=1
        else:
            answer.append(cnt)
            cnt=1
            mx=done
    answer.append(cnt)
    return answer