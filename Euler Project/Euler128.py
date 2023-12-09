#first generate primes
#fast prime sieve...
num_of_primes = 500
ps = [True]*num_of_primes
primes = [2]
for i in range(1, num_of_primes):
    if ps[i]:
        primes.append(x:=2*i+1)
        for p in range(2*(i*i+i),num_of_primes,x):
            ps[p] = False
primes = []
#better for this application prime sieve...
num_of_primes = 100_000_0
ps = [True]* num_of_primes
ps[0] = False
ps[1] = False
for i in range(2, 100000):
    if ps[i]:
        primes.append(i)
        for p in range(i*i, num_of_primes, i):
            ps[p] = False
#from the primes, generate the prime spiral 
pdn = [1,2]
ring_number = 1
#first top, then go around the sides, then finally add last item
tile_number = 2
while len(pdn)<2000:
    tile_number+=6*ring_number
    ring_number+=1
    #check each of the "corner" values

    #first one is special
    #check if the value is accurate
    if ps[ring_number*6-1] and ps[ring_number*6+1] and ps[6*(ring_number*2+1)-1]:
        pdn.append(tile_number)
    if ps[ring_number*6-1] and ps[ring_number*6+5] and ps[6*(ring_number*2-1)-1]:
        pdn.append(tile_number+6*ring_number-1)
print(len(pdn))
print(pdn[-1])
print(pdn)