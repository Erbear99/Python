file = open("Day2.txt", 'r')

values = [x.strip().split(" ") for x in file]
score = 0
for x, y in values:
    if y == "X":
        score+=1
    if y == "Y":
        score+=2
    if y == "Z":
        score+=3
    
    if (x == 'A' and y == 'X') or (x == 'B' and y == 'Y') or (x == 'C' and y == 'Z') :
        score+=3
    elif (x == 'A' and y == 'Y') or (x == 'B' and y == 'Z') or (x == 'C' and y == 'X'):
        score+=6
    else:
        score+=0
print(score)
score = 0
for x,y in values:
    if y == "X": #lose
        if x == "A":
            score+=3
        if x == "B":
            score+=1
        if x == "C":
            score+=2

    if y == "Y": #lose
        score+=3
        if x == "A":
            score+=1
        if x == "B":
            score+=2
        if x == "C":
            score+=3

    if y == "Z": #lose
        score+=6
        if x == "A":
            score+=2
        if x == "B":
            score+=3
        if x == "C":
            score+=1
print(score)
    

