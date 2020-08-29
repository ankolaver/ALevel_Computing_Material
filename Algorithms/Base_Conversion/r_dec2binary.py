def d2b(num):
    if num == 0 or num == 1:
        return num
    else:
        return str(d2b(num//2))+str(num%2)


print(d2b(56))
