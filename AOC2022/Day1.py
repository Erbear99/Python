file = open("Day1.txt", 'r')

values = [x.strip() for x in file]
elfsnacks = []
sum = 0
greatest = 0 
greatest_elf = 0
for i in values:
    if i == "":
        elfsnacks.append(sum)
        if sum > greatest:
            greatest = sum
        sum = 0
    else:
        sum+=int(i)
    
elfsnacks.append(sum)
print(max(elfsnacks))
elfsnacks.sort()
print(elfsnacks[-1]+ elfsnacks[-2]+elfsnacks[-3])
