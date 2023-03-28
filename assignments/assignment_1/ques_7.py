lower, upper, sc, dig = 0, 0, 0, 0

password = input("Enter password: ")

if (len(password) >= 6 and len(password) <= 16 ):
    for i in password:
        if (i.islower()):
            lower += 1           
        elif (i.isupper()):
            upper += 1           
        elif (i.isdigit()):
            dig += 1           
        elif(i=='@'or i=='$' or i=='_'):
            sc += 1          
if (lower>=1 and upper>=1 and sc>=1 and dig>=1 and lower+upper+sc+dig==len(password)):
    print("Valid Password")
else:
    print("Invalid Password")