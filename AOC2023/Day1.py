rows = [x.strip() for x in open("AOC2023/Day1.txt").readlines()]

total = 0
for x in rows:
   new_data = [y for y in x if y in "0123456789"]
   if len(new_data)>0:
    total+=int( new_data[0] + new_data[-1])
print(total)
total = 0


for x in rows:
  values = []
  for position, letter in enumerate(x):
    #find the posiitons of the letters
    if letter in "0123456789":
      values.append(int(letter))
    if x[position:position+3] == 'one':
      values.append(1)
    if x[position:position+3] == 'two':
      values.append(2)
    if x[position:position+5] == 'three':
      values.append(3)
    if x[position:position+4] == 'four':
      values.append(4)
    if x[position:position+4] == 'five':
      values.append(5)
    if x[position:position+3] == 'six':
      values.append(6)
    if x[position:position+5] == 'seven':
      values.append(7)
    if x[position:position+5] == 'eight':
      values.append(8)
    if x[position:position+4] == 'nine':
      values.append(9)
    if x[position:position+4] == 'zero':
      values.append(0)
  total+=int(str(values[0])+str(values[-1]))
print(total)