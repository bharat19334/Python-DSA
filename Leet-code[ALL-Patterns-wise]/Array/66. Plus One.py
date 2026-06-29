
def plusOne(digits):

        # rev = 0
        # for n in digits:
        #     rev = 10 * rev + n
        # new = rev + 1
        # box = []
        # for i in str(new):
        #     box.append(int(i))
        # return box

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
        
    return [1] + digits
    
digits = [1,2,4]
print(plusOne(digits))