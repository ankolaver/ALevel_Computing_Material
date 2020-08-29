def i_h2d(string):
    res = 0
    for temp,d in enumerate(string) : 
        value = "0123456789ABCDEF".index(d) 
        res += value*16**(len(string)-(temp+1))
    return res
print(i_h2d("63B"))
