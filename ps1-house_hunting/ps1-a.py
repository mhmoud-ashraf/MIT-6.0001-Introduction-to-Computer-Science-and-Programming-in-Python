# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 23:28:47 2019

@author: Mahmoud Ashraf
"""

annual_salary = int(input("Enter your annual salary:   "))
portion_saved = float(input("Enter portion of salary to \
be saved, as decimal:   "))
total_cost = int(input("Enter cost of your dream home:   "))

portion_down_payment = 0.25 * total_cost
current_savings = 0

number_of_months = 0
while current_savings < portion_down_payment:
    current_savings += portion_saved * annual_salary / 12 \
                    + current_savings * 0.04 / 12
    number_of_months += 1
    
print("Number of months:  " , number_of_months)