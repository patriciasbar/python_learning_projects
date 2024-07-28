# Task
# Given an integer, , perform the followng conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5 , print Not Weird
# If  is even and in the inclusive range of 6  to 20 , print Weird
# If  is even and greater than , print Not Weird
# Input Format

def weird_or_not(n):
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")

