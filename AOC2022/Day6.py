file = open("Day6.txt", 'r')

values = [x.strip() for x in file]
count = 0

string = values[0]
x = 0
contains = "   n"
while True:
    new_string = contains[1:] + string[x]
    single = True
    for i in new_string:
        if new_string.count(i) > 1:
            single = False
            break
    if single:
        print(new_string)
        break
    contains = new_string
    x+=1
print(x+1)

x = 0
contains = "              "
while True:
    new_string = contains[1:] + string[x]
    single = True
    for i in new_string:
        if new_string.count(i) > 1:
            single = False
            break
    if single:
        print(new_string)
        break
    contains = new_string
    x+=1
print(x+1)




        

