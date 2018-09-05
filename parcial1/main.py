# Jose Manuel Beauregard Mendez     A01021716
import pry

def lexer3(s):
    result = [''] * 100
    pos = 0
    for idx, i in enumerate(s):
        try:
            if int(i):
                num = int(i)
                if num < 0 or num > 3:
                    result[pos] = 'ERROR - Number is not in base 3'
                    return result 
                result[pos] += str(num)
        except ValueError:
            # Handling non numerical values
            if i == '.':
                # Checks that the previous value is a number
                if int(s[idx -1].isdigit()):
                    result[pos] += i
                else:
                    result[pos] = 'ERROR - No number left to the dot'
                    return result
            elif i == ' ' or i == ' ' or i == '\t' or i == '\n':
                pos += 1
            else:
                return result
    return result