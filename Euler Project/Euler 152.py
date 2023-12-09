#generate primes below the 
from math import lcm
max_value = 81
leastmultiple = 1
for x in range(2,max_value):
    leastmultiple = lcm(x*x, leastmultiple)

numerators = [leastmultiple//(x*x) for x in range(2,max_value)]
ideal_value = leastmultiple//2
impossible_values = []
linked_values = {x:[[x]] for x in range(2, max_value)} # initialize to none being linked


for i in range(2, max_value):
    #select the modularity of the values in order to determine whether they are possible as a solution
    modulos = [x%i for x in numerators]
    non_zeroes = [x for x,y in enumerate(modulos) if y!=0 and x not in impossible_values]
    #now try to create possible combinations for these values with the added exception that it must fill the required links 
    #there could be multiple options for a given thing to fall into...
    # From these values, give the possible sets that could arise from them... (including numbers and )
    starter_sets_with_duplicates = [(y, sum([modulos[xx] for xx in y])) for x in non_zeroes for y in linked_values.get(x)]
    #eliminate duplicates from the starter sets:
    starter_sets = []
    for set, modu in starter_sets_with_duplicates:
        valid = True
        for validated_set, modu in starter_sets:
            if len([x for x in validated_set if x not in set]) == 0 and len(set) == len(validated_set):
                valid = False
                break
            if not valid:
                break
        if valid:
            starter_sets.append((set, modu))
    print(linked_values[5])
    print(i, starter_sets, modulos)
    possibilities = []
    #generate possibilities by going left to right in the starter sets, and trying to add each value to the possibilities
    for set, modulo in starter_sets:
        new_possibilities = [(set, modulo)]
        for possible_set, possible_modulo in possibilities:
            #either don't add the new item to the set, or add a new item to the set
            new_possibilities.append((possible_set, possible_modulo))
            #for each value in the list of possibilities look to see if the new value would work. 
            #really what we are looking for is to see if the sets overlap but we can't have multiple of the same items.
            new_items = [x for x in possible_set if x not in set] # this means the items aren't currently in the set.
            if len(new_items) !=0: #if we are adding at least one new item... allow a new entry to be constructed.
                #first make sure the solution isn't already in the list
                valid = True
                for new_possible_set, new_possible_mod in new_possibilities:
                    total_set = [x for x in set]+[x for x in new_items]
                    if len([x for x in new_possible_set if x not in total_set]) == 0 and len(total_set) == len(new_possible_set):
                        valid = False
                        break
                if valid:
                    new_possibilities.append((total_set, ((modulo+sum([modulos[x] for x in new_items]))%i)))
        possibilities = new_possibilities
    solutions = [set for set, modulo in possibilities if modulo == 0]
    #now we have to update our impossible values and linked values:
    new_impossible_values = [x for x in non_zeroes if x not in [y for set in solutions for y in set]]
    #we also need to update all the linked values that are now impossible because one of the linked numbers is impossible.
    #the following values have solutions: check to see which of these solutions are the same...
    linked_solution_values = [y for set in solutions for y in set]
    print(solutions)
    new_links = {x:[solution for solution in solutions if x in solution] for x in linked_solution_values}
    #for index in new_links:
        #linked_values[index] = new_links[index]

    impossible_values = impossible_values+new_impossible_values
    print(impossible_values)


possible_numerators = [numerators[x] for x in range(0,max_value-2) if x not in impossible_values]
print([x+2 for x in range(0,max_value-2) if x not in impossible_values])
min_values = [ideal_value-sum(possible_numerators[x:]) for x in range(0,len(possible_numerators))]
#now go through and generate the combinations to see the possibilities
print(min_values)
count_of_solutions = 0
combinations = {0:1}

#combine the last 12 elements
final = [ideal_value]
for i in possible_numerators[-22:]:
    new_list = [x-i for x in final]
    final = final+new_list


for i in range(len(possible_numerators)-22):
    print(len(combinations), count_of_solutions, i,len(possible_numerators))
    new_combinations = {}
    for combination in combinations:
        #the value must be at least the same as the possible numerator
        if combination >= min_values[i]:
            if new_combinations.get(combination) is None:
                new_combinations[combination] = combinations[combination]
            else:
                new_combinations[combination] += combinations[combination]
        if combination + possible_numerators[i] < ideal_value:
            if new_combinations.get(combination + possible_numerators[i]) is None:
                new_combinations[combination + possible_numerators[i]] = combinations[combination]
            else:
                new_combinations[combination + possible_numerators[i]] += combinations[combination]
        elif combination + possible_numerators[i] == ideal_value:
            count_of_solutions+=combinations[combination]
            #print('Solution:',[numerators.index(possible_numerators[x])+2 for x in combination[1]+[i]])
    combinations = new_combinations



for i in final:
    if combinations.get(i) is not None:
        count_of_solutions+=combinations.get(i)

print(count_of_solutions)