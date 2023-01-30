import random

count_even = 0
count_odd = 0
count_prime = 0

def isPrime(num):
    flag = False
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            flag = True
            break  
    return flag 

num = [random.randrange(100,901) for i in range (0,100)]

for i in range (0,100):
    if num[i]%2 == 0:
        count_even += 1
    elif num[i]%2 != 0:
        count_odd += 1
        if isPrime(num[i]):
            count_prime += 1
   

print('No. of even numbers is: ' + str(count_even))
print('No. of odd numbers is: ' + str(count_odd))
print('No. of prime numbers is: ' + str(count_prime))