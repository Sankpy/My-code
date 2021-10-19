#we need to find out what is leap year
def year(n):
    Examined_year=n
    return Examined_year%4==0 and (Examined_year%100!=0 or Examined_year%400==0)
year(int(input()))