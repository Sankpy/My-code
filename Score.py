# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:11:17 2022

@author: Sanket Banerjee
"""

def score():
    try:
        score_of_student=float(input("Enter your score = "))
        if  score_of_student >=0.0 and score_of_student<0.6:
            return("F")
        elif score_of_student >=0.6 and score_of_student<0.7:
            return ("D")
        elif score_of_student >=0.7 and score_of_student<0.8:
            return ("C")
        elif score_of_student >=0.8 and score_of_student<0.9:
             return("B")
        elif score_of_student >=0.9 and score_of_student<=1.0:
             return ("you get the highest score A")
        elif score_of_student<0.0 or score_of_student>1.0:
              return ("There is a range buddy admit it")
    except ValueError :
            return("Enter  float numbers only")
print(score())