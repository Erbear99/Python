
def digital_sum(num):
    remainder = num
    sqrt = 0
    sum = 0
    for _ in range(100): # do this 100 times
        newval = 0
        while (((20*sqrt+(newval+1)) * (newval+1)) <=remainder):
            newval+=1
        remainder = (remainder - (20*sqrt + newval)*newval)*100
        sqrt = sqrt*10+newval
        sum+=newval
    return sum

total = 0
for i in range(1,100):
    if i not in (1,4,9,16,25,36,49,64,81,100):
        print(i, digital_sum(i))
        total += digital_sum(i)
print(total)

    