rows = [x.strip() for x in open("AOC2023/Day5.txt").readlines()]

seeds = []
other_vals = []
seed_to_soil = []
soil_to_fert = []
fert_to_water = []
water_to_light = []
light_to_temp = []
temp_to_humid = []
humid_to_lccat = []

last_row = ''
for row in rows:
    if ':' in row: # try to switch states
        if 'seeds: ' in row:
            seeds = [int(x) for x in row[7:].split(" ")]
        else:
            other_vals.append([])
    elif row == '':
        pass
    else:
        other_vals[-1].append([int(x) for x in row.split(" ")])

locations = []
for seed in seeds:
    #find the match in all the corresponding values:
    value = seed
    for map in other_vals:
        for x in map:
            if x[1] <=value <x[1] + x[2]:
                value = x[0] + value-x[1]
                break
    locations.append(value)
print(min(locations))

prev_poss = []

for i in range(len(seeds)//2): #pairs of seeds 
    #find the match in all the corresponding values:
    #0 = initial value, #1 = length
    prev_poss.append([seeds[2*i], seeds[2*i+1] ])

for map in other_vals:
    current_list = []
    possibilities = [x for x in prev_poss]
    for x in map:
        source_start = x[1]
        source_end = x[1]+x[2]-1
        new_poss = []
        for val in possibilities:
            poss_start = val[0]
            poss_end = val[0] + val[1] - 1
            #either split into multiple parts ooorrr give the new possibilities
            if poss_end < source_start or poss_start > source_end:
                new_poss.append(val)
            elif poss_start < source_start and poss_end > source_end:
                #possibility needs to be split into multiple parts
                current_list.append([x[0], x[2]])
                new_poss.append([poss_start, source_start-poss_start])
                new_poss.append([source_end+1, poss_end-source_end])
            elif poss_start < source_start and poss_end <= source_end:
                current_list.append([x[0], poss_end-source_start+1])
                new_poss.append([poss_start, source_start-poss_start])
            elif poss_start >= source_start and poss_end > poss_end:
                current_list.append([x[0]+(poss_start-source_start), source_end-poss_start+1])
                new_poss.append([source_end+1, poss_end-source_end])
            else:
                current_list.append([x[0]+(poss_start-source_start), val[1]])
        possibilities = new_poss
    #after going through all the possibilities, convert the final ones directly.
    for x in possibilities:
        current_list.append(x)
    prev_poss = current_list


minimum_location = 10000000000
for x in prev_poss:
    minimum_location = min(minimum_location, x[0])
print(minimum_location)