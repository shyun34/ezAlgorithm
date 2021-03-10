def solution(number, k):
    number = list(number)
    rest_num = len(number) - k
    new_list = []

    number2 = number[:k]
    index_first = number2.index(max(number2))

    for i in range(index_first):
        number.pop(0)

    while len(number) > rest_num:

        if number[0] < number[1]:
            number.pop(0)
        else:
            new_list.append(number[0])
            number.pop(0)
            rest_num -= 1

    # print("new_list :",new_list)
    # print("number :",number)
    for i in range(len(number)):
        new_list.append(number[i])

    answer = ''.join(new_list)

    return answer

if __name__ := '__main__':

    number = "4177252841"
    k = 4
    print("answer :",solution(number,k))