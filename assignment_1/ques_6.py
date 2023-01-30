basic_salary = float(input('Enter your basic salary: '))

if basic_salary > 0 and basic_salary <= 10000: 
    hra = .2 * basic_salary
    da = .8 * basic_salary
    gross_salary = basic_salary+hra+da
    print('Your gross salary is ' + str(gross_salary))

elif basic_salary > 10000 and basic_salary <= 20000: 
    hra = .25 * basic_salary
    da = .9 * basic_salary
    gross_salary = basic_salary+hra+da
    print('Your gross salary is '+ str(gross_salary))

else:
    hra = .3 * basic_salary
    da = .95 * basic_salary
    gross_salary = basic_salary+hra+da
    print('Your gross salary is ' + str(gross_salary))


