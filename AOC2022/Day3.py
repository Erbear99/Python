file = open("Day3.txt", 'r')

values = [x.strip() for x in file]
sum = 0
for i in values:
    c1 = i[:len(i)//2]
    c2 = i[len(i)//2:]
    for i in c1:
        if i in c2:
            oldsum = sum
            if i == i.upper():
                sum+=ord(i)-64+26
            else:
                sum+=ord(i)-96
            break
print(sum)

group_no = 0
sum = 0

while group_no<len(values):
    for i in values[group_no]:
        if i in values[group_no+1] and i in values[group_no+2]:
            if i == i.upper():
                sum+=ord(i)-64+26
            else:
                sum+=ord(i)-96
            break
    group_no+=3
print(sum)
