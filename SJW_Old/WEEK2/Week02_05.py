def solution(s):
    answer = ''

    #문자열 리스트로 변환
    arr = s.split(" ")

    intArr = []
    for i in arr:
        intArr.append(int(i))
    
    #정렬
    intArr.sort()

    #시작 항과 끝 항 문자열 변환
    answer = str(intArr[0]) + " " + str(intArr[len(intArr) - 1])

    print("answer : ",answer)
    return answer


if __name__ == "__main__":
    #input
    s = "-1 -2 -3 -4"

    solution(s)