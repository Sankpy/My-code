import math
def square(number):
    multiple=number*number
    return multiple
def sum(limit):
    add=0
    for number in range(limit):
        add+=square(number)
    return(add)
print(sum(10),math.sqrt(sum(10)))