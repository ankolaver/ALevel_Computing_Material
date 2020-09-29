def r_d2h(num):
    if num>=16:
        return d2h(num/16)+"0123456789ABCDEF"[int(num%16)]
    else:
        return "0123456789ABCDEF"[int(num%16)]
    
d2h(1595)
