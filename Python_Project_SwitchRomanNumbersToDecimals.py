#Switch Roman Numbers to Decimals
#LeetCode question
roman= {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def RomanNumeralToDecimal(romantrans):
    sum = 0
    for i in range(len(romantrans)-1):
        left = romantrans[i]
        right = romantrans[i+1]
        if roman[left] < roman[right]:
            sum -= roman[left]
        else:
            sum += roman[left]
    sum += roman[romantrans[-1]]
    return sum
roman_input = input("Enter Roman number:")
RomanNumeralToDecimal(roman_input)