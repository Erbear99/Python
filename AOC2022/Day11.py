file = open("Day11.txt", 'r')

values = [x.strip() for x in file]

monkies = []
monkey_oper = []
monkey_test = []
monkey_true = []
monkey_false = []
line_no = 1
while line_no< len(values):
    monkies.append([int(x) for x in values[line_no].split(": ")[1].split(', ')])
    monkey_oper.append(values[line_no+1].split(" = ")[1].split(" ")[1:])
    monkey_test.append(int(values[line_no+2].split(" ")[-1]))
    monkey_true.append(int(values[line_no+3].split(" ")[-1]))
    monkey_false.append(int(values[line_no+4].split(" ")[-1]))
    line_no+=7


new_monkies = []
for x in monkies:
    new_monkey_items = []
    for y in x:
        new_items = []
        for div in monkey_test:
            new_items.append(y%div)
        new_monkey_items.append(new_items)
    new_monkies.append(new_monkey_items)



inspections = [0 for _ in range(len(monkies))]
rounds = 20
for i in range(rounds):
    for monkey_no, values in enumerate(monkies):
        for item in values:
            inspections[monkey_no]+=1
            worry_level = item
            if monkey_oper[monkey_no][0] == '*':
                if monkey_oper[monkey_no][1] == 'old':
                    worry_level *=worry_level
                else:
                    worry_level *=int(monkey_oper[monkey_no][1])
            else:
                worry_level+=int(monkey_oper[monkey_no][1])
            worry_level = worry_level//3
            if worry_level % monkey_test[monkey_no] ==0:
                monkies[monkey_true[monkey_no]].append(worry_level)
            else:
                monkies[monkey_false[monkey_no]].append(worry_level)
        monkies[monkey_no] = []
inspections.sort()
print(inspections[-1]*inspections[-2])


inspections = [0 for _ in range(len(monkies))]
rounds = 10000
for i in range(rounds):
    for monkey_no, monkeys_items in enumerate(new_monkies):
        for item_list in monkeys_items:
            inspections[monkey_no]+=1
            for monkey_item_pos, monkey_item in enumerate(item_list): #perform worry operation
                worry_level = monkey_item 
                if monkey_oper[monkey_no][0] == '*':
                    if monkey_oper[monkey_no][1] == 'old':
                        worry_level *=worry_level
                    else:
                        worry_level *=int(monkey_oper[monkey_no][1])
                else:
                    worry_level+=int(monkey_oper[monkey_no][1])
                item_list[monkey_item_pos] = worry_level % monkey_test[monkey_item_pos]
            if item_list[monkey_no] == 0:
                new_monkies[monkey_true[monkey_no]].append(item_list)
            else:
                new_monkies[monkey_false[monkey_no]].append(item_list)    
        new_monkies[monkey_no] = []
inspections.sort()
print(inspections[-1]*inspections[-2])


