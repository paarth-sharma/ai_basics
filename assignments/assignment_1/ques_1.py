x = int(input("enter a integer:"))
n = int(input("enter the no. of terms"))
t = 1
sum = 0
for j in range (1,n+1):
    t = (t*x)/j
    sum = sum+t

print("sum is equal to:",sum+1)