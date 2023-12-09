file = open("Day19.txt", 'r')
blueprints = [[int(z) for pos, z in enumerate(x.strip().split(" ")) if pos == 6 or pos == 12 or pos == 18 or pos == 21 or pos == 27 or pos ==30] for x in file]
#O, O, O C, OOB
quality_levels = 0
#ore, clay, obsidian, geode
time = 24
for bpno, blueprint in enumerate(blueprints):
    #simulate best possible scneario in 24 seconds


    starting_vals = [([0,0,0,0], [1,0,0,0], 0)]

    #real depth first search with recursion

    max_time = 24
    max_geodes = 0
    while len(starting_vals)>0:
        new_starting_vals = []
        for resources, robots, time in starting_vals:
            #try to build each new type of robot
            if time >= max_time:
                if time == max_time:
                    if resources[3] > max_geodes:
                        max_geodes = resources[3]
            else:

                #build ore robot

                if robots[0]< max(blueprint[1], blueprint[2], blueprint[4]):
                    if blueprint[0]<=resources[0]:
                        nre = [resources[0]+robots[0]-blueprint[0],resources[1]+robots[1],resources[2]+robots[2],resources[3]+robots[3]]
                        nro = [robots[0]+1, robots[1], robots[2], robots[3]]
                        new_starting_vals.append((nre, nro, time+1))
                    else:
                        rounds = 1
                        while blueprint[0] - resources[0] - rounds*robots[0] >0 and time+rounds+1<max_time:
                            rounds+=1
                        rounds+=1
                        nre = [resources[0]+robots[0]*rounds, resources[1]+robots[1]*rounds, resources[2]+robots[2]*rounds, resources[3]+robots[3]*rounds]
                        if time+rounds<max_time:
                            nre[0]-=blueprint[0]
                        nro = [robots[0]+1, robots[1], robots[2], robots[3]]
                        new_starting_vals.append((nre, nro, time+rounds))

                #build clay robot

                if robots[1]< blueprint[3]:
                    if blueprint[1]<=resources[0]:
                        nre = [resources[0]+robots[0]-blueprint[1],resources[1]+robots[1],resources[2]+robots[2],resources[3]+robots[3]]
                        nro = [robots[0], robots[1]+1, robots[2], robots[3]]
                        new_starting_vals.append((nre, nro, time+1))
                    else:
                        rounds = 1
                        while blueprint[1] - resources[0] - rounds*robots[0] >0 and time+rounds+1<max_time:
                            rounds+=1
                        rounds+=1
                        nre = [resources[0]+robots[0]*rounds, resources[1]+robots[1]*rounds, resources[2]+robots[2]*rounds, resources[3]+robots[3]*rounds]
                        if time+rounds<max_time:
                            nre[0]-=blueprint[1]
                        nro = [robots[0], robots[1]+1, robots[2], robots[3]]
                        new_starting_vals.append((nre, nro, time+rounds))

                #build obsidian robot
                if robots[2]< blueprint[5]:
                    if blueprint[2]<=resources[0] and blueprint[3]<=resources[1]:
                        nre = [resources[0]+robots[0]-blueprint[2],resources[1]+robots[1]-blueprint[3],resources[2]+robots[2],resources[3]+robots[3]]
                        nro = [robots[0], robots[1], robots[2]+1, robots[3]]
                        new_starting_vals.append((nre, nro, time+1))
                    else:
                        rounds = 1
                        while (blueprint[2] - resources[0] - rounds*robots[0] >0 or blueprint[3]-resources[1] -rounds*robots[1]>0) and time+rounds+1<max_time:
                            rounds+=1
                        rounds+=1
                        nre= [resources[0]+robots[0]*rounds, resources[1]+robots[1]*rounds, resources[2]+robots[2]*rounds, resources[3]+robots[3]*rounds]
                        if time+rounds<max_time:
                            nre[0]-=blueprint[2]
                            nre[1]-=blueprint[3]
                        nro = [robots[0], robots[1], robots[2]+1, robots[3]]
                        new_starting_vals.append((nre,nro,time+rounds))

                #build Geode robot

                if blueprint[4]<= resources[0] and blueprint[5]<=resources[2]:
                    nre = [resources[0]+robots[0]-blueprint[4],resources[1]+robots[1],resources[2]+robots[2]-blueprint[5],resources[3]+robots[3]]
                    nro = [robots[0], robots[1], robots[2], robots[3]+1]
                    new_starting_vals.append((nre, nro, time+1))
                else:
                    rounds = 1
                    while (blueprint[4] - resources[0] - rounds*robots[0] >0 or blueprint[5]-resources[2] -rounds*robots[2]>0) and time+rounds+1<max_time:
                        rounds+=1
                    rounds+=1
                    nre= [resources[0]+robots[0]*rounds, resources[1]+robots[1]*rounds, resources[2]+robots[2]*rounds, resources[3]+robots[3]*rounds]
                    if time+rounds<max_time:
                        nre[0]-=blueprint[4]
                        nre[2]-=blueprint[5]
                    nro = [robots[0], robots[1], robots[2], robots[3]+1]
                    new_starting_vals.append((nre,nro,time+rounds))
        starting_vals = new_starting_vals
       
    quality_levels+=max_geodes*(bpno+1)
print(quality_levels)



def factorial(integer):
    x = 0
    for i in range(1, integer+1):
        x+=i
    return x


largest_num = 1
for blueprint in blueprints[:3]:
    #simulate best possible scneario in 24 seconds

    starting_vals = [([0,0,0,0], [1,0,0,0], 0)]

    #real depth first search with recursion

    max_time = 32
    max_geodes = 0
    while len(starting_vals)>0:
        new_starting_vals = []
        for resources, robots, time in starting_vals:
            #try to build each new type of robot
            if time >= max_time:
                if time == max_time:
                    if resources[3] > max_geodes:
                        max_geodes = resources[3]
                        print(max_geodes)
            elif max_geodes-resources[3]>robots[3]*(max_time-time)+factorial(max_time-time):
                continue
            else:

                #build ore robot

                if robots[0]< max(blueprint[1], blueprint[2], blueprint[4]):
                    if blueprint[0]<=resources[0]:
                        nre = [resources[0]+robots[0]-blueprint[0],resources[1]+robots[1],resources[2]+robots[2],resources[3]+robots[3]]
                        nro = [robots[0]+1, robots[1], robots[2], robots[3]]
                        new_starting_vals.append((nre, nro, time+1))
                    else:
                        rounds = 1
                        while blueprint[0] - resources[0] - rounds*robots[0] >0 and time+rounds+1<max_time:
                            rounds+=1
                        rounds+=1
                        nre = [resources[0]+robots[0]*rounds, resources[1]+robots[1]*rounds, resources[2]+robots[2]*rounds, resources[3]+robots[3]*rounds]
                        if time+rounds<max_time:
                            nre[0]-=blueprint[0]
                        nro = [robots[0]+1, robots[1], robots[2], robots[3]]
                        new_starting_vals.append((nre, nro, time+rounds))

                #build clay robot

                if robots[1]< blueprint[3]:
                    if blueprint[1]<=resources[0]:
                        nre = [resources[0]+robots[0]-blueprint[1],resources[1]+robots[1],resources[2]+robots[2],resources[3]+robots[3]]
                        nro = [robots[0], robots[1]+1, robots[2], robots[3]]
                        new_starting_vals.append((nre, nro, time+1))
                    else:
                        rounds = 1
                        while blueprint[1] - resources[0] - rounds*robots[0] >0 and time+rounds+1<max_time:
                            rounds+=1
                        rounds+=1
                        nre = [resources[0]+robots[0]*rounds, resources[1]+robots[1]*rounds, resources[2]+robots[2]*rounds, resources[3]+robots[3]*rounds]
                        if time+rounds<max_time:
                            nre[0]-=blueprint[1]
                        nro = [robots[0], robots[1]+1, robots[2], robots[3]]
                        new_starting_vals.append((nre, nro, time+rounds))

                #build obsidian robot
                if robots[2]< blueprint[5]:
                    if blueprint[2]<=resources[0] and blueprint[3]<=resources[1]:
                        nre = [resources[0]+robots[0]-blueprint[2],resources[1]+robots[1]-blueprint[3],resources[2]+robots[2],resources[3]+robots[3]]
                        nro = [robots[0], robots[1], robots[2]+1, robots[3]]
                        new_starting_vals.append((nre, nro, time+1))
                    else:
                        rounds = 1
                        while (blueprint[2] - resources[0] - rounds*robots[0] >0 or blueprint[3]-resources[1] -rounds*robots[1]>0) and time+rounds+1<max_time:
                            rounds+=1
                        rounds+=1
                        nre= [resources[0]+robots[0]*rounds, resources[1]+robots[1]*rounds, resources[2]+robots[2]*rounds, resources[3]+robots[3]*rounds]
                        if time+rounds<max_time:
                            nre[0]-=blueprint[2]
                            nre[1]-=blueprint[3]
                        nro = [robots[0], robots[1], robots[2]+1, robots[3]]
                        new_starting_vals.append((nre,nro,time+rounds))

                #build Geode robot

                if blueprint[4]<= resources[0] and blueprint[5]<=resources[2]:
                    nre = [resources[0]+robots[0]-blueprint[4],resources[1]+robots[1],resources[2]+robots[2]-blueprint[5],resources[3]+robots[3]]
                    nro = [robots[0], robots[1], robots[2], robots[3]+1]
                    new_starting_vals.append((nre, nro, time+1))
                else:
                    rounds = 1
                    while (blueprint[4] - resources[0] - rounds*robots[0] >0 or blueprint[5]-resources[2] -rounds*robots[2]>0) and time+rounds+1<max_time:
                        rounds+=1
                    rounds+=1
                    nre= [resources[0]+robots[0]*rounds, resources[1]+robots[1]*rounds, resources[2]+robots[2]*rounds, resources[3]+robots[3]*rounds]
                    if time+rounds<max_time:
                        nre[0]-=blueprint[4]
                        nre[2]-=blueprint[5]
                    nro = [robots[0], robots[1], robots[2], robots[3]+1]
                    new_starting_vals.append((nre,nro,time+rounds))
        starting_vals = new_starting_vals
       
    print(max_geodes)
    largest_num*=max_geodes
print(largest_num)