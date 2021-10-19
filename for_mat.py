def leap_year(n):
    if n%4==0 and (n%400==0 or n%100!=0):
       print(True)
leap_year(int(input()))