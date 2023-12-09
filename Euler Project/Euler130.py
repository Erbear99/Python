
num_of_primes = 100_000_0
ps = [True]* num_of_primes
ps[0] = False
ps[1] = False
for i in range(2, 100000):
    if ps[i]:
        for p in range(i*i, num_of_primes, i):
            ps[p] = False


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

local_max = 0
composite_vals = []
start = 1
while len(composite_vals)<25:
    start+=1

    #find first resp...
    if ps[start] == False and gcd(start,10) == 1:
        #do the long division as they go....
        a = 1
        q = 1
        #start with enough 1's to cover the val... then find the remainder... from there count the number of 1's left unitl remainder = 0
        while q!=0:
            a+=1
            q = (q*10+1)%start
        if (start-1) % a == 0:
            composite_vals.append(start)
            print(start, a)
print(sum(composite_vals))