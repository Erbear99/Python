
n = 10**8
#generate all the gaussian integer pairs:
def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

total = 0

for i in range(1,n+1):
    total+= i* (n//i)
    #for j in range(i, n-n%i+1, i):
    #    total+=i
print("part 1 done")

#define just the integers values
for integer_part in range(1, int((n**.5))+1):
    for complex_part in range(1, int((n-integer_part**2)**.5)+1):
        if gcd(integer_part, complex_part) == 1: #make sure that the values are co-prime
            #add the values as well as the factors to the list
            basic_denominator = integer_part**2+complex_part**2
            #basic denominator
            count = 0
            for i in range(basic_denominator, n-n%basic_denominator+1, basic_denominator):
                count+=1
                total+=2*integer_part*count*(n//i)
                #for j in range(i, n-n%i+1, i): #given the current denominator, generatre all the possible values 
                #    total+=2*integer_part*count




print(total)