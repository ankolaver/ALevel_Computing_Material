import time
primes = []

start = time.time() #start of program
for a in range(1,2000):
    primes.append(a)


count = [2,3,5,7,11]
for c in count:
    for b in primes:
        if b in count:
            continue
        elif b%c==0:
            primes.remove(b)
            count.append(b)
print(primes)
end = time.time()

print("The prime program to calculate 1000 primes took:",(end-start),"sec")
    


testcases = int(input("How many primes to test:"))
for testcase in range(0,testcases):
    num = int(input("Enter the index of the prime number: "))
    print(primes[num])
