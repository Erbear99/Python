#generate primes
import math

maxval = 50000000

ivals = [1]*int(math.sqrt(maxval))
ps = []

curr_i = 2
while curr_i < len(ivals):
    if ivals[curr_i] != 0:
        ps.append(curr_i)
        remove = curr_i**2
        while remove<len(ivals):
            ivals[remove] = 0
            remove+=curr_i
    curr_i+=1



prime_squares = [x**2 for x in ps]
prime_cubes = [x**3 for x in ps if x**3<maxval]
prime_fourth = [x**4 for x in ps if x**4<maxval]

list_of_vals = []
for x in prime_squares:
    for y in prime_cubes:
        for z in prime_fourth:
            if x+y+z<maxval:
                list_of_vals.append(x+y+z)
print(len(set(list_of_vals)))