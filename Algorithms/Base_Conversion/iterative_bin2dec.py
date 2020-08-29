def b2d(num):
    fin = power = 0
    while num>0:
        fin += 2**power*(num%10)
        num //=10
        power += 1
    return fin
print(b2d(111000))
