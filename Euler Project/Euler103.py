#first thing...
#generate sets that are possible 

#then look at distances and decide what the starting value would be for the set... and thus the sum
n = 7

#generate adding pattern

#distances =
half_val = (n-1)/2
addends = [x+((-abs(x-half_val)+half_val)*n) for x in range(n-1,0, -1)] 
max_set_sum = 10000000


possibilities = {tuple(1 for x in range(n-1)):sum(addends)}
possibilitiesv2 = {}

while len(possibilities) > 0:
    possibilitiesv2 = {}
    for possibility in possibilities:
        #try to add a new thing... add it to the set. 
        #check to see if the current value works!!!
        if possibilities[possibility]> max_set_sum:
            continue
        initial_val = sum([((-abs(x-half_val)+half_val)*y) for x,y in enumerate(possibility)])+1
        newvals = [initial_val]
        for x in possibility:
            newvals.append(newvals[-1]+x)

        #Generate subset sums
        rule2 = True
        for number_in_subsets in range(2,n//2+1):
            subset_sums = {}
            #generate the combos
            current_pos = [i for i in range(number_in_subsets)]
            while current_pos[0]+number_in_subsets<= n and rule2:
                #check the sum for matches in the dict
                subset_sum = sum([newvals[x] for x in current_pos])
                if subset_sums.get(subset_sum) is None:
                    subset_sums[subset_sum] = [tuple(x for x in current_pos)]
                else:
                    #check to make sure that the values have an overlap
                    for different_pos in subset_sums[subset_sum]:
                        if len([val for val in current_pos if val in different_pos]) == 0:# lists don't overlap
                            rule2 = False
                            break
                    if rule2:
                        subset_sums[subset_sum].append(tuple(x for x in current_pos))
                #increment the position
                incremented = False
                for i in range(1,number_in_subsets+1):
                    if current_pos[-i] !=n-i and not incremented:
                        incremented = True
                        current_pos[-i]+=1
                        for j in range(1,i):
                            current_pos[-(i-j)]=current_pos[-i]+j
                if not incremented:
                    current_pos[0]+=1
            if not rule2:
                break
        if rule2:
            max_set_sum = min(max_set_sum, sum(newvals))
            print(newvals, sum(newvals))
        for pos, val in enumerate(addends):
            if possibilities[possibility] + val < max_set_sum:
                possibilitiesv2[tuple(possibility[x] if x!= pos else possibility[x]+1 for x in range(n-1))] = possibilities[possibility] + val
    possibilities = possibilitiesv2

