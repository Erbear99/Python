
class Node:
    def __init__(self, number, data, next=None):
        self.number = number
        self.data = data
        self.next = next
    def __str__(self) -> str:
        return str(f"Number: {self.number}  chance:{self.data}")




blue_node = Node(15, 15*14)
addend = 15
max_node = blue_node

while addend <= 20:
    max_node.next = (tmp_node:= Node(addend+1, max_node.data+addend*2))
    max_node = tmp_node
    addend+=1

import random

users = ['Erik','Ethan','Carl','Seth','Jacob','Spencer']

random.shuffle(users)
print(users)

print(f'team1 {users[:3]}')
print(f'team2 {users[3:]}')



while addend <1000000000000:
    if blue_node.data*2 > max_node.data:
        max_node.next = (tmp_node:= Node(addend+1, max_node.data+addend*2))
        max_node = tmp_node
        addend+=1
    elif blue_node.data*2 == max_node.data:
        print(blue_node, max_node)
        blue_node = blue_node.next
    else:
        blue_node = blue_node.next

 