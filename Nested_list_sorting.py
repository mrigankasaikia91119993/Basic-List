# python script to find the lowest marks holder in a nested list of students with their marks in alphabetical order
#at first we will make our nested list
a = int(input("enter no of students\n"))
reg = [[] for i in range(a)]
for i in range(a):
    name = input("Enter name all in small caps\n")
    marks = float(input("Enter marks\n"))
    reg[i].append(name)
    reg[i].append(marks)
# now we will sort our nested list using the lambda function and key argument    
func = lambda x: x[1]
reg.sort(key = func)
# now we check for the lowest holder and check if there is more then one holding the same lowest marks
c = 0
for p in range(a):
    if reg[0][1] == reg[p][1]:
        c += 1 
lis = []       
for u in range(c):
    lis.append(reg[u][0])
lis.sort()
print(lis)
    
    