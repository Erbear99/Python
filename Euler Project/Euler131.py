#generate cubes

num_of_primes = 100_000_0
ps = [True]* num_of_primes
ps[0] = False
ps[1] = False
for i in range(2, 100000):
    if ps[i]:
        for p in range(i*i, num_of_primes, i):
            ps[p] = False



cubes = [x**3 for x in range(100000)]

for n, cube1 in enumerate(cubes):
    if n == 0:
        continue
    divisor = n*n
    for n2, cube2 in enumerate(cubes[n+1:]):
        if (cube2-cube1) % divisor == 0:
            x = (cube2-cube1) // divisor
            if x < 100000 and ps[x]:
                print(n, n+n2+1, x)
                break