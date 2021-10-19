def is_power_of_two(n):
        while (n%2==0) and (n>1):
# Check if the number can be divided by two without a remainder
              return True
        if n==1:
           return True
        else:
            return False
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False