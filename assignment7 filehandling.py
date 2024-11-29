#assignment 7 filehandling
file = open('newman.txt','r')
lines = file.readlines()
for line in lines:
    print(line)
file.close()
