import sys
from collections import Counter
sys.stdin = open("input.txt","rt")
#4:08 ~ 4:25


def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for idx, val in enumerate(phone_book):
        if idx == len(phone_book) -1 :
            break
        elif phone_book[idx+1].find(val) == 0:
            return False
    return answer

if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123","456","789"]))
    print(solution(["12","123","1235","567","88"]))
    print(solution(["112","44","4544"]))
    

    
