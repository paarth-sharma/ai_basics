x = int(input("enter a year:"))
y = int(input("enter another year:"))

for i in range(x,y+1):
    if ((i%4==0) or (i%100==0 and i%400==0)):
        print(i," is a leap year")