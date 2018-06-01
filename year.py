"""This program define the season of year by number of month"""
def season(num_of_month):
    if num_of_month == 12:
        print("It's winter!")
    elif num_of_month <= 2:
        print("It's Winter!")
    elif num_of_month >= 3:
        if num_of_month <= 5:
            print("It's Spring!")
    elif num_of_month >= 6:
        if num_of_month <= 8:
            print("It's Summer!")
    elif num_of_month >= 9:
        if num_of_month <= 11:
            print("It's Autumn!")
print("Enter the number of month: ")
a = int(input())
season(a)