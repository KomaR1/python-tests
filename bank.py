"""This program is counting your profit and total amount of your deposit"""
def bank(a,years):
    days = years * 365
    profit = int((a * 0.1 * days)/365)
    print("Your profit is: ", profit)
    print("Your total amount is: ", profit+a)

print("Enter the amount of money at 10% per annum:")
m = int(input())
print("Enter the number of years:")
z = int(input())
bank(m,z)
