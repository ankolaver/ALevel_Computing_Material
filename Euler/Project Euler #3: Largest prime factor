import math 
numtest = int(input("How many test cases?: "))
final = []
for i in range(0,numtest):
    store = []
    def primeFactors(n): 
        while n % 2 == 0: 
            store.append(2) 
            n = n / 2
              

        for i in range(3,int(math.sqrt(n))+1,2): 
            while n % i== 0: 
                store.append(i) 
                n = n / i      

        if n > 2: 
            store.append(n) 
              
    primeFactors(int(input("Enter a factorizable no: ")))

    final.append(int(max(store)))

for k in final:
    print(k)
