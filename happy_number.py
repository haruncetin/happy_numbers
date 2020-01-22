def is_happy(num):
    # smallest happy number after 1 is 7
    while num > 6: # 1'den sonraki en küçük mutlu sayı 7
        result = 0
        digits = []
        temp = num
        while(temp>0):
            digits.append(temp%10)
            temp = temp // 10
        while(digits != []):
            digit = digits.pop()
            result = result + digit * digit
        num = result

    return num==1

for num in range(99999):
    if is_happy(num):
        print(num , "is a HAPPY number!")
