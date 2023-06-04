import os
import shutil
# Read file
script_dir = os.getcwd()
os.mkdir('root')
os.chdir('root')
root_dir = os.getcwd()
with open(script_dir+'/'+'input.txt', 'r') as puzzle:
    for puzzle_line in puzzle:
        puzzle_line = puzzle_line.rstrip('\r\n')
        # Directory creation
        if puzzle_line == '$ cd /':
            os.chdir(root_dir)
        elif puzzle_line == '$ cd ..':
            os.chdir('..')
        elif puzzle_line[0:5] == '$ cd ':
            current_address = os.getcwd()
            subdir = puzzle_line[5:len(puzzle_line)]
            if not os.path.exists(current_address+'/'+subdir):
                os.mkdir(subdir)
            os.chdir(current_address+'/'+subdir)
        # File creation
        elif puzzle_line[0].isnumeric():
            file_line = puzzle_line.split(" ")
            file_name = file_line[0]
            file = open(file_name, 'x')
            file.close()
# Create list of directory name & total file size tuples
os.chdir(root_dir)
tuples = []
def recurse(path):
    dir_name = path.split('\\')[-1]
    size_list = []
    for x in os.walk(path):
        for y in x[-1]:
            size_list.append(int(y))
    size_sum = sum(size_list)
    tuple = (dir_name, size_sum)
    if tuple not in tuples:
        tuples.append((dir_name, size_sum))
    for x in os.walk(path):
        if x[0] != path:
            recurse(x[0])
recurse(root_dir)
# Sum directories with sizes under 100000
large_dirs = []
large_dirs_sum = 0
for tuple in tuples:
    if tuple[1] <= 100000:
        large_dirs_sum += tuple[1]
# Find the smallest directory to delete
deletion_candidates = []
for tuple in tuples:
    if tuple[1] >= (30000000-(70000000-tuples[0][1])):
        deletion_candidates.append(tuple[1])
deletion_candidates.sort()
# Wipe files
os.chdir(script_dir)
shutil.rmtree('root')
# Print solutions
print("The solution to part 1 is", large_dirs_sum)
print("The solution to part 2 is", deletion_candidates[0])