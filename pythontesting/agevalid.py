# validation workflow
'''
valid_age = False
while not valid_age:
    age = input("Enter age: ")
    # presence check
    if len(age) == 0:
        print("Empty input")
    # data type check
    elif not age.isdigit():
        print("Age must be a number")
    # range check
    elif not 0 < int(age) < 100:
        print("Age must be between 1 and 99")
    # valid age
    else:
        valid_age = True
        
print("ok")
'''
#actual running
def age_valid(age):
    if age=='':
        msg = "Empty input"
        return msg
    # data type check
    elif type(age)==str:
        msg = "Age must be a number"
        return msg
    # range check
    elif not 0 < age < 100:
        msg = "Age must be between 1 and 109"
        return msg
    # valid age
    else:
        valid_age = True
