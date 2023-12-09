file = open("Day4.txt", 'r')

values = [x.strip() for x in file]

count=0
for i in values:
    temp = i.split(",")
    temp2 = temp[0].split('-')
    temp3 = temp[1].split('-')
    if (int(temp2[0]) <= int(temp3[0]) and int(temp2[1])>=int(temp3[1])) or (int(temp2[0]) >= int(temp3[0]) and int(temp2[1])<=int(temp3[1])):
        count+=1
print(count)

count=0
for i in values:
    temp = i.split(",")
    temp2 = [int(x) for x in temp[0].split('-')]
    temp3 = [int(x) for x in temp[1].split('-')]
    if (temp2[0]<=temp3[0] and temp2[1]>=temp3[0]) or (temp2[0]<=temp3[1] and temp2[1]>= temp3[1]) or temp2[0]>=temp3[0] and temp2[1]<= temp3[1]:
        count+=1
print(count)