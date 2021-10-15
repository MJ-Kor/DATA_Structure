num = int(input("num 값을 입력하시오 : "))
pow_num = int(input("power 값을 입력하시오 : "))
res = 1
while pow_num:
    if (pow_num % 2) == 1:
        res = res * num
    pow_num = pow_num // 2
    num = num * num

print(res)

