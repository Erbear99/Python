
pentagon_nums = []

for i in range(1,100000):
    pentagon_nums.append((3*i**2-i)//2)
    pentagon_nums.append((3*i**2+i)//2)


partitions = [1]

for i in range(1,1000000):
    #generate the numbers
    #first add the next two nums, then subtract.. etc
    sum = 0
    pent_pos = 0
    looping = True
    while looping:
        if i-pentagon_nums[pent_pos]>=0:
            if pent_pos % 4 == 0:
                sum+=partitions[i-pentagon_nums[pent_pos]]
            else:
                sum-=partitions[i-pentagon_nums[pent_pos]]
        else:
            looping = False
        if i-pentagon_nums[pent_pos+1]>=0:
            if pent_pos % 4 == 0:
                sum+=partitions[i-pentagon_nums[pent_pos+1]]
            else:
                sum-=partitions[i-pentagon_nums[pent_pos+1]]
        else:
            looping = False
        pent_pos+=2
    partitions.append(sum)
    if sum %1000000 == 0:
        print(sum, i)