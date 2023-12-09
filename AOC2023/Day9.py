rows = [x.strip() for x in open("AOC2023/Day9.txt").readlines()]
final_values = []
left_most_values = []
for x in rows:
    extrapolated_values = []
    values = [int(y) for y in x.split(" ")]
    while len([x for x in values if x !=0])!=0:
        extrapolated_values.append(values)
        values = [values[x+1]-values[x] for x in range(len(values)-1)]
    extrap_val = 0
    left_most_value = 0
    for x in extrapolated_values[::-1]:
        extrap_val+=x[-1]
        left_most_value= x[0] - left_most_value
    final_values.append(extrap_val)
    left_most_values.append(left_most_value)
print(sum(final_values))
print(sum(left_most_values))
