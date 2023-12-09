
import time
import math

start = time.time()
n=10
#first generate the primes needed to ensure the new number isn't prime
number_of_primes = int(10**(n/2))
prime_sieve = [True]*number_of_primes
primes = []
for p in range(2,number_of_primes):
    if prime_sieve[p]:
        primes.append(p)
        for i in range(p*p, number_of_primes, p):
            prime_sieve[i] = False
print(primes)       

#start by assuming the best
maxes = {i:n for i in range(10)}
number = {i:0 for i in range(10)}
sums = {i:0 for i in range(10)}

#generate masks as well as numbers for the outstanding digits

#first generate masks

#these will be n long, but will use the max values
while len([i for i in sums if sums[i] ==0])!=0:
    #select these values, subtract 1 from their maxes and check this new selection
    #generate the values for the mask (what the value is multiplied by)
    check_digits = [i for i in sums if sums[i]==0]
    for digit in check_digits:
        maxes[digit]-=1
        new_number = maxes[digit]
    #pick number of digits out of n
    chosen_vals = [i for i in range(new_number)]
    #generate choices

    choices = []
    while True:
        choices.append((sum([10**i for i in chosen_vals]), [10**i for i in range(n) if i not in chosen_vals]))
        #try to update value
        changed = False
        for i in range(1,len(chosen_vals)+1):
            if chosen_vals[-i] != n-i:
                chosen_vals[-i]+=1
                changed = True
                for j in range(1,i):
                    chosen_vals[-(i-j)] = chosen_vals[-(i-j+1)]+1
                break
        if not changed:
            break
    print(choices)

    #Generate digits of a certain length
    digits = [0]*(n-new_number)
    while True:
        #generate the number corresponding to the digits
        for addend, multiplicand in choices:
            new_val = sum([x*multiplicand[pos] for pos,x in enumerate(digits)])
            for check_digit in check_digits:
                new_sum = new_val+addend*check_digit
                #make sure it is an n digit number and also make sure that it doesn't repeat the digit being checked
                if new_sum < 10**(n-1):
                    continue
                if check_digit in digits:
                    continue
                #check if the new_sum is prime
                is_prime = True
                for p in primes:
                    if new_sum%p == 0:
                        is_prime = False
                        break
                if is_prime: #if it is prime, add it to the sum
                    number[check_digit]+=1
                    sums[check_digit]+=new_sum

        #increment the digits unless you cant, then break
        changed = False
        for i in range(1, len(digits)+1):
            if digits[-i] != 9:
                digits[-i] +=1
                changed = True
                break
            else:
                digits[-i] = 0
        if not changed:
            break






print(sums)
print(number)
print(maxes)
print(sum([sums[i] for i in sums]))