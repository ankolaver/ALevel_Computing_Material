numtestcase = int(input("enter testcases: "))
store = []
multiples = 0
for a in range(0,numtestcase):
    store.append(int(input("enter test subjects: ")))

for b in store:
    for c in range(0,b):
        if c%5==0 or c%3==0:
            multiples+=c
    print(multiples)
