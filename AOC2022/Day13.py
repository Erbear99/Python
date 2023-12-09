file = open("Day13.txt", 'r')
values = [x.strip() for x in file]


def compare_packets(packet1, packet2):
    #check if both values are lists
    if len(packet1) == 0 and len(packet2) == 0:
        return 0
    if len(packet1)==0:
        return 1
    if len(packet2)==0:
        return -1
    if packet1[0] == '[' and packet2[0] == '[':
        #seperate the lists
        list1 = []
        list2 = []
        temp_var = ""
        brackets = 0
        for x in packet1[1:-1]:
            if x == ',' and brackets == 0:
                list1.append(temp_var)
                temp_var = ''
            elif x == '[':
                temp_var+=x
                brackets+=1
            elif x == ']':
                temp_var+=x
                brackets-=1
            else:
                temp_var+=x
        list1.append(temp_var)
        temp_var = ""
        brackets = 0
        for x in packet2[1:-1]:
            if x == ',' and brackets == 0:
                list2.append(temp_var)
                temp_var = ''
            elif x == '[':
                temp_var+=x
                brackets+=1
            elif x == ']':
                temp_var+=x
                brackets-=1
            else:
                temp_var+=x
        list2.append(temp_var)
        if len(list1) < len(list2):
            for x in range(len(list1)):
                temp = compare_packets(list1[x], list2[x])
                if temp != 0:
                    return temp
            return 1
        if len(list2) < len(list1):
            for x in range(len(list2)):
                temp = compare_packets(list1[x], list2[x])
                if temp != 0:
                    return temp
            return -1
        if len(list1) == len(list2):
            for x in range(len(list2)):
                temp = compare_packets(list1[x], list2[x])
                if temp != 0:
                    return temp
            return 0
    if packet1[0] != '[' and packet2[0] != '[':
        if int(packet1) < int(packet2):
            return 1
        elif int(packet2) < int(packet1):
            return -1
        else:
            return 0
    if packet1[0] != '[':
        return compare_packets('['+packet1+']', packet2)
    else:
        return compare_packets(packet1, '['+packet2+']')
        



i =0
right_order = 0
while i<len(values):
    if compare_packets(values[i], values[i+1]) == 1:
        right_order+=(i//3 + 1)
    i+=3

print(right_order)

sorted_values = ['[[2]]','[[6]]']
#now order the packets
i =0
while i<len(values):
    new_position = len(sorted_values)
    while new_position>0 and compare_packets(sorted_values[new_position-1], values[i]) == -1:
        new_position-=1
    sorted_values = sorted_values[:new_position] +[values[i]]+sorted_values[new_position:]
    new_position = len(sorted_values)
    while new_position>0 and compare_packets(sorted_values[new_position-1], values[i+1]) == -1:
        new_position-=1
    sorted_values = sorted_values[:new_position] +[values[i+1]]+sorted_values[new_position:]
    i+=3


#find decoder keys, multiply them
decoder1 = 0
decoder2 = 0
for pos, value in enumerate(sorted_values):
    if value == '[[2]]':
        decoder1 = pos+1
    if value == '[[6]]':
        decoder2 = pos+1
print(decoder1*decoder2)