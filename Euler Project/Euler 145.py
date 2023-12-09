
total = 0
for i in range(1000000000):
    stringver = str(i)
    if stringver[-1] !='0':
        reversedval = stringver[::-1]
        combined = int(stringver)+int(reversedval)
        even = [x for x in str(combined) if int(x)%2 == 0]
        if len(even) ==0:
            total+=1

print(total)


#    1000000000< 

#for even digits
#


