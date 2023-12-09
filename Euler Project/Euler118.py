#generate the primes through 1000000000
import time

start = time.time()
number_of_primes = int(100000000)
prime_sieve = [True]*number_of_primes
primes = []
for p in range(2,number_of_primes):
    if prime_sieve[p]:
        x = str(p)
        if '0' not in x and len(set(x)) == len(x):
            primes.append(x)
        for i in range(p*p, number_of_primes, p):
            prime_sieve[i] = False
  

count = 0
def anagramic_prime(max_index, current_primes, current_string):
    global count
    if len(current_string) == 9:
        print(current_primes)
        count+=1
    for i in range(max_index):
        prime = primes[i]
        if len(prime)+len(current_string)>9:
            break
        if len(prime+current_string) > len(set(prime+current_string)):
            continue
        anagramic_prime(i,current_primes+(prime,), prime+current_string)

for pos, val in enumerate(primes):
    anagramic_prime(pos, (val,), val)


print(time.time()-start)

#sort by sizes
