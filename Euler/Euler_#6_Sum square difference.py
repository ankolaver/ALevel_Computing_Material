testcases = int(input("How many testcases: "))

for a in range(0, testcases):
    num = int(input("Enter number: "))
    naturalsum = 0
    squaresum = 0
    for b in range(0,num+1):
        naturalsum += (b**2)
        squaresum += b
    squaresum = squaresum**2
    print(squaresum-naturalsum)
