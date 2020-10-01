# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:03:36 2020

@author: rahul
"""
import math
month_number=0
annual_salary=float(input("How much do you make?"))
total_cost=1000000
semi=0.07
portion_down_payment = 0.25*total_cost
current_savings = 0
r=0.04
bis=0
guess=0
low=0
high=10000
while(abs(guess-portion_down_payment)>100):    
    portion_saved=round(((low+high)/2)/10000,10)
#Note: 1.04*3(total investment multiplier)=3.12    
    if(annual_salary*3.12<portion_down_payment):
        break
    bis+=1
    while(month_number<36):
        monthly_salary=(annual_salary/12)*((1+semi)**(math.floor(month_number/6)))
        amt_saved=portion_saved*monthly_salary
        current_savings+=current_savings*(r/12)
        current_savings+=amt_saved
        month_number+=1
    guess=current_savings
    if(abs(guess-portion_down_payment)<100):
        break
    elif(guess<portion_down_payment):
        low=portion_saved*10000
        current_savings=0
        month_number=0
    elif(guess>portion_down_payment):
        high=portion_saved*10000
        current_savings=0
        month_number=0
        
    
if(annual_salary*3.12<portion_down_payment):
    print("It is not possible to pay the down payment in three years.")
else:      
    print("Here is your savings rate: " + str(round(portion_saved,4)))
    print("Number of bisections: " + str(bis))