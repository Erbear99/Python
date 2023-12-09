#for a given number

n = 7

#sets of 2 and 3 for seven
for set_size in range(2,n//2+1):
    #number of possibilities
    #ex 7 choose 4 and 7 choose 6
    #times the number of distinct solutions to the problem for the given set (size of 4... orders such that a set of two will not both be larger or smaller. possibly requiring one value to stay in palce for non-duplicates.)
    #check choose x from 2x
    positions = [x for x in range(2*set_size)]
    #choose two
    position = [x for x in range(set_size)]
    oppisite = [x for x in positions if x not in position]
    print(position, oppisite)