rows = [x.strip() for x in open("AOC2023/Day2.txt").readlines()]



count= 0
for row in rows:
    x = row.split(':')
    y = x[1].split(';')
    valid = True
    for z in y:
        zz = z.split(',')
        for letters in zz:
            letter = letters.split(' ')  
            if letter[2] == 'red' and int(letter[1])>12:
                valid = False
            if letter[2] == 'green' and int(letter[1])>13:
                valid = False
            if letter[2] == 'blue' and int(letter[1])>14:
                valid = False

    if valid:
        count+=int(x[0][5:])
print(count)


power = 0
for row in rows:
    x = row.split(':')
    y = x[1].split(';')
    minimum = {'red':0, 'green':0, 'blue':0}
    for z in y:
        zz = z.split(',')
        for letters in zz:
            letter = letters.split(' ')
            if int(letter[1]) > minimum[letter[2]]:
                minimum[letter[2]] = int(letter[1])

    power+= minimum['red']*minimum['green']*minimum['blue']
print(power)
