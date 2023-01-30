d={1:"one",2:"two",3:"three",4:"four",5:"five"}
print(d)

d[6]="six"
print(d)

del d[2]
print(d)

if 6 in d:
    print("exists")
else:
    print("dne")

count = 0
for (key,value) in d.items():
    count=count+1
print(count)

sum = 0
for key in d:
    sum=sum+key
print(sum)