basic_salary =int(input("Enter your gross salary : "))
benefits =int(input("Enter your benefits : "))
gross_salary = basic_salary + benefits

def nhif():
    if gross_salary <6000:
        nh = 150
    elif 6000> gross_salary<7999:
        nh =    300
    elif 8000>gross_salary<11999:
        nh =400
    elif 12000 >gross_salary< 14999:
        nh=500
    elif 15000 >gross_salary< 19999:
        nh=600
    elif 20000 >gross_salary< 24999:
        nh=750
    elif 25000 >gross_salary< 29999:
        nh=850
    elif 30000 >gross_salary< 34999:
        nh=900
    elif 35000 >gross_salary< 39999:
        nh=950
    elif 40000 >gross_salary< 44999:
        nh=1000
    elif 45000 >gross_salary< 49999:
        nh=1100
    elif 50000 >gross_salary< 59999:
        nh=1200
    elif 60000 >gross_salary< 69999:
        nh=1300
    elif 70000 >gross_salary< 79999:
        nh=1400
    elif 80000 >gross_salary< 89999:
        nh=1500
    elif 90000 >gross_salary< 99999:
        nh=1600
    elif gross_salary>= 100000:
        nh= 1700

    return (nh)

nh = nhif()
print( 'nhif =',nh)

# def  nssf():
#     ns = 6/100 * gross_salary
#     return ns
# ns =int(nssf())
# print("Nssf= ",ns)

# def taxable_income():
#     ti=gross_salary-ns
#     return ti
# ti = taxable_income()
# print("Txable_income =", ti)



# Task 21: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nssf + payee)

