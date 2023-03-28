l = [10,20,30,40,50,60,70,80]
print(l)
l.append(200)
l.append(300)

print("appended list:",l)
l.pop(0)
l.pop(2)
print("new list:",l)

temp = 0
for i in range(0, len(l)):    
    for j in range(i+1, len(l)):    
        if(l[i] > l[j]):    
            temp = l[i]  
            l[i] = l[j]    
            l[j] = temp
print(l)

for i in range(0, len(l)):    
    for j in range(i+1, len(l)):    
        if(l[i] < l[j]):    
            temp = l[i]  
            l[i] = l[j]    
            l[j] = temp
print(l)