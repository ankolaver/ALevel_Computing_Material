def productval(num):
    if len(str(num))!=5:
        msg = "Code is too short or too long. Within 5 characters"
        return msg
    #check ascii for uppercase
    elif ord(str(num)[0])>90 or ord(str(num)[0])<64:
        msg = "First letter should be alphabatical and in CAPS"
        return msg

    elif (ord(i)>57 for i in (str(num)[1:])) or (ord(i)<48 for i in (str(num)[1:])) :
        msg = "symbols or letters present"
        return msg
        
    
