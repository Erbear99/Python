# generate combinations of discs that win


n = 15
numerator = 1
denominator = 1
for i in range(n):
    denominator*=i+2
print(denominator)

for i in range((int((n-1)/2)//1)):
    #this generates the number of elements needed to select
    base_elements = [x+1 for x in range(i+1)]
    #add the element to the numerator
    incremented = True
    while incremented:
        added_num = 1
        for x in base_elements:
            added_num*=x
        numerator+=added_num
        #increment the element
        incremented = False
        for i in range(1, len(base_elements)+1):
            if base_elements[-i] != n+1-i:
                base_elements[-i] +=1
                #update the following elements
                for j in range(1,i):
                    base_elements[-(i-j)] = base_elements[-(i-j+1)]+1
                incremented = True
                break

print(numerator)
print(denominator)

print(denominator/numerator)