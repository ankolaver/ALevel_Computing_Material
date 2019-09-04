def luhn(credit_num):
    doubarr = []
    count = len(str(credit_num))
    print(count)
    if count%2==0: #Even
        while count>1:
            doubarr.append((str(credit_num)[count-1]))
            doubarr.append(str(int(str(credit_num)[count-2])*2))
            count-=2
        print("Even route",doubarr)
    else: #odd
        while count>=1:
            
            doubarr.append((str(credit_num)[count-1]))
            doubarr.append(str(int(str(credit_num)[count-2])*2))
            count-=2
        del doubarr[-1]
        print("Odd route", doubarr)
        

    #summing large digits
    for idx,val in enumerate(doubarr):
        if int(val)>9:
            del doubarr[idx]
            
            newval = str(int(str(val)[:1])+int(str(val)[1:]))
            doubarr.insert(idx,newval)
    print("This is the updated:\n", doubarr)

    #adding digits together, and check
    checksum = 0
    for num in doubarr:
        checksum+=int(num)
    print("Checksum",checksum)
    if checksum%10==0:
        print("True")
    else:
        print("False")
    
luhn(4148634548477380)
luhn(4148634548477385)
luhn(79927398713)
