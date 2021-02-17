def solution(s):
    nums = list(map(int,s.split(' ')))
    print(nums)
    large = max(nums)
    small = min(nums)
    answer = str(small)+' '+str(large)
    return answer