import math
import time

print(time.process_time())
sum = 10
primes = [2,3,5]
for i in range(7, 2000000,2):
    is_prime = True
    for prime in primes:
        if prime >math.sqrt(i):
            break
        if i%prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
        sum+=i
print(sum)
time2 = time.process_time()

n = 2000000
m = (n-1) // 2
b = [True]*m
i,p,ps = 0,3,[2]
while p*p < n:
    if b[i]:
        ps.append(p)
        j = 2*i*i + 6*i + 3
        while j < m:
            b[j] = False
            j = j + 2*i + 3
    i+=1; p+=2
while i < m:
    if b[i]:
        ps.append(p)
    i+=1; p+=2

print (time2, time.process_time()-time2)
