digit_count = 0
current_number = 0
total_value = 0

#22_786_974_071
possible = True
while possible:
    difference = current_number-digit_count
    if difference > 0:
        pass
    elif difference < 0:
        pass
    else:
        total_value+=digit_count
        print(digit_count, total_value)
        current_number+=1
        digit_count+=sum([1 for x in str(current_number) if x == 1])

