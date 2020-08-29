def r_h2d(string,num,length):
    res = 0
    if num<length:
        curr = string[num].lower() 
        res+="0123456789abcdef".index(curr)*16**(length-num-1) 
        return res+r_h2d(string,num+1,length)
    else:
        return res      
        
print(r_h2d("63B",0,len("63B")))
