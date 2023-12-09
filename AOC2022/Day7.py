file = open("Day7.txt", 'r')

values = [x.strip() for x in file]
directories = []

current_dir = []

filesize = {'':0}


for line in values:
    if line.startswith("$ cd /"): continue
    if line.startswith("$ ls"): continue
    if line == "$ cd ..":
        current_dir = current_dir[:-1]
        continue
    if line.startswith("$ cd "):
        current_dir.append(line[5:])
        continue
    if line.startswith("dir "):
        filesize["/".join(current_dir+[line[4:]])] = 0
        directories.append("/".join(current_dir+[line[4:]]))
    else:
        filesize["/".join(current_dir)] += int(line.split(" ")[0])



dirs_sizes = {
        x:sum( filesize[file]
        for file in filesize
        if file.startswith(x))
    for x in directories
}

total= 0
for i in dirs_sizes:
    if dirs_sizes[i] < 100000:
        total+=dirs_sizes[i]

print(total)

total_space = sum(filesize.values()) - 40000000

ideal_removal = 300000000

for i in dirs_sizes.values():
    if i > total_space:
        if i < ideal_removal:
            ideal_removal = i
print(ideal_removal)
