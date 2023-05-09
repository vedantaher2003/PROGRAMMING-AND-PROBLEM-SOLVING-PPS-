print("HELLO USERS!")
'''
PROBLEM STATEMENT:
Write a Program in Python to calculate salary of an employee given
his basic pay (take as input from user). Calculate gross salary of
employee. Let HRA be 10 % of basic pay and TA be 5% of basic
pay. Let employee pay professional tax as 2% of total salary.
Calculate net salary payable after deductions.
'''
employee_name=input('Please enter your name:')
employee_id = ('Please enter your id:')
basic_pay = float(input("Enter basic pay"))
if(basic_pay>0):
    hra = basic_pay * 0.1
    ta = basic_pay * 0.05
    tsa = basic_pay + hra + ta
    tax = 0.02 * tsa
    gsal = tsa - tax
    print("Employee name:" + employee_name)
    print("Employee id:" + employee_id)
    print("Home rent allowance:" + str(hra))
    print("Travel allowance:" + str(ta))
    print("Total Salary:" + str(tsa))
    print("Tax:" + str(tax))
    print("Gross salary:" + str(gsal))
else:
    print("Please enter valid basic pay")