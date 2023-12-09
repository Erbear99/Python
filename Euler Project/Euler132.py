num_of_primes = 100_000_0
ps = [True]* num_of_primes
ps[0] = False
ps[1] = False
primes = []
for i in range(2, num_of_primes):
    if ps[i]:
        primes.append(i)
        for p in range(i*i, num_of_primes, i):
            ps[p] = False

first40factors = []
base = [10**x for x in range(10)]
repunit = 1
for i in range(0):
    new_repunit = 0
    for j in range(10):
        new_repunit+=base[j]
    factors = []
    for p in primes:
        if len(first40factors) == 40 and p>first40factors[-1]:
            break
        x,y = divmod(new_repunit, p)
        if y == 0:
            new_repunit = x
            factors.append(p)
            print(factors)
            first40factors.append(p)
            first40factors.sort()
            first40factors = first40factors[:40]
    print(first40factors)
    print(len(first40factors))
    if i != 9:
        #increment the bases
        base[1] = base[1] * base[9]
        for j in range(1,9):
            print(i,j)
            base[j+1] = base[j] * base[1]
    


#my first try failed so here I am....


#fucking around with multiplicitave orders......

total = 40
#just do this for 11 but in the future develop an algorithm....
grand_total = 0
for p in primes[2:]:
    remainders = {}
    #determine the multiplicative order of 10 (mod p)
    remainder = 10
    order = 1
    while True:
        remainder = remainder%p
        if remainder == 1:
            #generate the correct order......
            temp = order
            i = 0
            j = 0
            while temp%2 == 0:
                i+=1
                temp//=2
            while temp%5 == 0:
                j+=1
                temp//=5
            if temp == 1:
                if max(i,j)<=9:
                    grand_total+=p
                    total-=1
                    print(40-total, order, i, j)
                    if total == 0:
                        print('final grand ',grand_total)
                        while True:
                            pass
            break
        if remainders.get(remainder) is not None:
            print(f'Not Found:      p {p}     N  {remainders}')
            break
        remainders[remainder] = True
        order+=1
        remainder*=10





