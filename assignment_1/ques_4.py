l=[]
p=[]
g=[]

x = int(input("enter the amount of numbers you want in first list:"))
y = int(input("enter the amount of numbers you want in second list:"))
for i in range(1,x+1):
    a = int(input("enter a number:"))
    l.append(a)

for j in range(1,y+1):
    b = int(input("enter a number for the second list:"))
    p.append(b)

if (x<y):
    for k in range(0,x):
        if l[k]==p[k]:
            g.append(p[k])
else:
    for k in range(0,y):
        if l[k]==p[k]:
            g.append(p[k])
print(g)