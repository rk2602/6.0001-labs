# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:03:36 2020

@author: rahul
"""
import math
month_number=0
annual_salary=float(input("How much do you make?"))
portion_saved=float(input("How much do you save (give decimal form of percentage)?"))
total_cost=float(input("How much does your dream house cost?"))
semi=float(input("What's your semi-annual raise?"))
portion_down_payment = 0.25*total_cost
current_savings = 0
r=0.04
while(current_savings<portion_down_payment):
    monthly_salary=(annual_salary/12)*((1+semi)**(math.floor(month_number/6)))
    amt_saved=portion_saved*monthly_salary
    current_savings+=current_savings*(r/12)
    current_savings+=amt_saved
    month_number+=1
    print(current_savings)
    
print("this is the number of months it'll take: " + str(month_number))