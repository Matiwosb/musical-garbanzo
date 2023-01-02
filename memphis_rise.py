"""
Paycheck Calculator

Author: Matiwos Birbo
"""


def paycheck_calc(wage, hours_wrk):
    # You will need an if-elif statement right here
    # All of your code needs to be in the function
    print("Employee Name: " + employee_name)  # Displays employee name
    regular_hour = 40  # regular hour = 40
    reg_hour_pay = wage * regular_hour  # regular hour pay rate is wage * 40
    regular_pay = wage * hours_wrk  # regular pay is the wage times the numbers of hour the person worked
    over_time_pay = wage * 1.5 * (hours_wrk - regular_hour)  # Over time pay = wage times 1.5 times the over hour
    # minus regular hour
    total_pay = over_time_pay + reg_hour_pay  # total pay is over time pay + regular hour pay

    if regular_hour == hours_wrk:  # checks the regular hour equals hours worked if it
        print("Paycheck Amount: " + str(regular_pay))  # if it equals it prints out the paycheck amount
    else:  # if it is not it prints out the over time pay
        print("Overtime Pay: " + str(over_time_pay))  # and the total paycheck amount
        print("Paycheck Amount: " + str(total_pay))


print("Welcome to Memphis Rise Paycheck Calculator")
employee_name = input("Enter the employee name: ")
wages = float(input("Enter the hourly rate: "))
hours_wrk = int(input("Enter number of whole hours worked: "))

paycheck_calc(wages, hours_wrk)  # this is a function call, do not change this line
# (you can change the variable names in the parentheses)
