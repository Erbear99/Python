import requests

#given day
request = requests.get('https://adventofcode.com/2022/day/6/input', cookies= {"session": "Use your session cookie"}) #replace with session cookie


file = open("Day6.txt", 'w')
file.write(request.text)
