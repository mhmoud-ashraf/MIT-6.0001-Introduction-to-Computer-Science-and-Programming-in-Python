# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 02:07:50 2019

@author: Mahmoud Ashraf
"""

annual_salary = int(input("Enter your starting annual salary:   "))
total_cost = 1000000
semi_annual_raise = 0.07

portion_down_payment = 0.25 * total_cost
current_savings = 0

steps_in_bisection_search = 0
low = 0
high = 10000

guess = int((low + high) / 2)
guessed_savings_rate = guess / 10000



def savings (current_savings , portion_down_payment , \
             annual_salary , semi_annual_raise , guessed_savings_rate):
    
    for number_of_months in range(0 , 36):
        if number_of_months % 6 == 0 and number_of_months != 0:
            annual_salary += annual_salary * semi_annual_raise
            
        current_savings += guessed_savings_rate * annual_salary / 12 \
                        + current_savings * 0.04 / 12
                        
    return current_savings



current_savings = savings (0 , portion_down_payment , \
                           annual_salary , \
                           semi_annual_raise , high/10000)

if current_savings < portion_down_payment:
    print ("Unfortunately, it is not possible to pay for the down payment \
           in 36 months :(")
else:
    current_savings = savings (0 , portion_down_payment , \
                               annual_salary , \
                               semi_annual_raise , guessed_savings_rate)
    steps_in_bisection_search += 1
    
    while abs(portion_down_payment - current_savings) >= 100:
        if  portion_down_payment > current_savings:
            low = guess
        else:
            high = guess
        guess = int((low + high) / 2)
        guessed_savings_rate = guess / 10000
        
        current_savings = int(savings (0 , portion_down_payment , \
                                   annual_salary , semi_annual_raise , \
                                   guessed_savings_rate))
        steps_in_bisection_search += 1

    print("Best savings rate:  " , guessed_savings_rate)
    print("Steps in bisecton search:  " , steps_in_bisection_search)