#prime sieve
import time

number_of_primes = int(1000)
prime_sieve = [True]*number_of_primes
primes = []
for p in range(2,number_of_primes):
    if prime_sieve[p]:
        x = p
        primes.append(x)
        for i in range(p*p, number_of_primes, p):
            prime_sieve[i] = False



start = time.time()
count = 0
for i in range(50000):
    for j in range(i):
        if (j*j)%i == 0:
            count+=1
print ('base approach: ',time.time()-start)


start = time.time()
count = 0

for i in range(50000):
    addend = -1
    curr_val = 0
    for j in range(i):
        addend = (addend+2)%i
        curr_val = (curr_val +addend)%i
        if curr_val == 0:
            count+=1
print ('test approach',time.time()-start)



