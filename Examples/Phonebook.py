numinput = int(input())
phonebook = {}
for a in range(0,numinput):
    name,number = input().split(" ")
    name = str(name)
    phonebook[name]=number

while True:
    request = input()
    a = phonebook.get(request)
    if a ==None:
        print("Not found")
    else:
        print("{0}={1}".format(request,a))
    
