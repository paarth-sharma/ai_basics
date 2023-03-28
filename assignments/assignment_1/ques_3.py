x = int(input("enter first number:"))
y = int(input("enter second number:"))
count_prime = 0

def isPrime(num):
    flag = False
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            flag = True
            break  
    return flag

for i in range(x, y + 1):
   if i > 1:
    if isPrime(i):
        count_prime += 1

print('No. of primes between '+ str(x) + ' and ' + str(y)+' is: ' + str(count_prime))