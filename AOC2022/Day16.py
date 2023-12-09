file = open("Day16.txt", 'r')
values = [x.strip() for x in file]
tunnels = {y.split(" ")[1]:(int(y.split(" ")[4].split("=")[1][:-1]), [yy[-2:] for yy in y.split(", ")]) for y in values}

minutes = 30
broken_valves = [x for x in tunnels if tunnels[x][0] == 0]


#generate distances to other non-broken valves for each valve
distances = {}
for tunnel in tunnels:
    if tunnel not in broken_valves or tunnel == 'AA':
        second_dict = {}
        depth = 1

        options = tunnels[tunnel][1]
        visited = []
        while len(options)>0:
            new_options = []
            for value in options:
                visited.append(value)
                if value not in broken_valves and second_dict.get(value) is None:
                    second_dict[value] = depth
                for value2 in tunnels[value][1]:
                    if value2 not in visited and value2 not in new_options:
                        new_options.append(value2)
            options = new_options
            depth+=1
        distances[tunnel] = second_dict
            

#turned valves, rate, pressure_released, time_left
possibilities = [(('AA',), 0, 0, 30)]
maxval = 0
while len(possibilities)>0:
    np = []
    for poss in possibilities:
        maxval = max(maxval, poss[2] + poss[1]*poss[3])
        cv = poss[0][-1]
        for nv in distances[cv]:
            if nv not in poss[0] and distances[cv][nv]<poss[3]:
                np.append((poss[0]+(nv,), poss[1]+tunnels[nv][0], poss[2]+ poss[1]*(distances[cv][nv]+1), poss[3]-(distances[cv][nv]+1)))
    possibilities = np

print(maxval)

maxvalues = {}

possibilities = [(('AA',), 0, 0, 26)]
maxval = 0
while len(possibilities)>0:
    np = []
    for poss in possibilities:
        maxstring = list(poss[0])
        maxstring.sort()
        maxstring = tuple(maxstring)
        if maxvalues.get(maxstring) is None:
            maxvalues[maxstring] = poss[2] + poss[1]*poss[3]
        else:
            maxvalues[maxstring] = max(maxvalues.get(maxstring), poss[2] + poss[1]*poss[3])
        cv = poss[0][-1]
        for nv in distances[cv]:
            if nv not in poss[0] and distances[cv][nv]<poss[3]:
                np.append((poss[0]+(nv,), poss[1]+tunnels[nv][0], poss[2]+ poss[1]*(distances[cv][nv]+1), poss[3]-(distances[cv][nv]+1)))
    possibilities = np

maxval = 0
for x1 in maxvalues:
    for x2 in maxvalues:
        if len(set(x1+x2))==len(x1+x2[1:]):
            maxval = max(maxvalues[x1] + maxvalues[x2], maxval)
print(maxval)



