#generate powers of numbers up to the point where it no longer makes sense

digit_power_sums = []


for i in range(2,100): #generate powers up to the point where the number of digits exceeds the number
    value = i
    iterations = 1
    while len(str(value*i))<i:# this doesn't quite work. For example- 10
        value = value*i
        iterations+=1
        print(i, sum([int(x) for x in str(value)]))
        if sum([int(x) for x in str(value)]) == i: #sum the digits 
            digit_power_sums.append((i,iterations, value))

digit_power_sums.sort(key= lambda x: x[2])
print(digit_power_sums[29])