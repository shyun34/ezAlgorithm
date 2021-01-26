from typing import ByteString

def caluate(formalar):
    
    anwer = 0
    temp = 1
    oprStack = []
    i = 0
    for operrand in formalar :
        
        if operrand == '(' :
            oprStack.append(operrand)
            temp *= 2

        elif operrand == '[':
            oprStack.append(operrand)
            temp *= 3

        elif operrand == ')':
            if '(' == oprStack[-1] and formalar[i-1] not in (')' , ']') :
                anwer += temp
            temp /= 2        
            oprStack.pop()
        elif operrand == ']':
            if '[' == oprStack[-1] and formalar[i-1] not in (')' , ']') :
                anwer += temp
            temp /= 3
            oprStack.pop()
        
        i += 1

    return anwer
 
print(caluate('(()[[]])([])'))
