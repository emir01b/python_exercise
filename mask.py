def mask_number(number):
    if len(number) < 4 :
        return number
    else :
        maskNumber = '#' * (len(number) - 4)
        return maskNumber
    
number = "1234567890"
print (mask_number(number) + number[-4:])