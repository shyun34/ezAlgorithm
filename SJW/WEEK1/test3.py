def solution(N,K):
    
    index = K-1
    nextNum = index
    arr = []
    retArr = []
    
    i = 1
    while i <= N:
        arr.append(i)
        i += 1

    while len(arr) > 0 :
        if nextNum < len(arr) :
            retArr.append( arr[nextNum])
            del arr[nextNum]
            nextNum += index
        else :
            nextNum -= len(arr)
            if(nextNum < len(arr)):
                retArr.append( arr[nextNum])
                del arr[nextNum]
                nextNum += index
   
    return retArr            
                

print(solution(7,4))            