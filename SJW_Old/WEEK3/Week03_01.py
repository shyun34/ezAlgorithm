from collections import deque
import math
"""
def fib(n):
    if(n==1 or n ==2):
        return 1
    return  fib(n-1) + fib(n-2)
"""

#메모이제이션
"""
dic = {}
def fib_memo(n):
    if n in dic.keys():
        return dic[n]

    if(n == 0):
        dic[n] = 0
        return 0
    if(n == 1):
        dic[n] = 1
        return 1
    else:
        dic[n] = fib_memo(n - 1) + fib_memo(n - 2)
        return fib_memo(n-1) + fib_memo(n-2)
"""

#상향식
"""
def fib(n):
    if n <= 1:
        return n
    return memoize(n)


def memoize(n):
    cache = {0: 0, 1: 1}

    for i in range(2, n + 1):
        cache[i] = (cache[i - 1] + cache[i - 2]) % 1234567

    return cache[n]
"""

#하향식
cache = [-1]*100001
def fib(N: int) -> int:
    if N <= 1:
        return N
    return memoize(N)

def memoize(N: int) -> {}:
    if cache[N] != -1 :
        return cache[N]
    cache[N] = (memoize(N - 1) + memoize(N - 2)) % 1234567
    return memoize(N)

def solution(n):
    # output
    answer = 0
    dic = {}

    answer = fib(n) % 1234567

    print("answer : ",answer)
    return answer


if __name__ == "__main__":
    #input
    n = 3

    solution(n)