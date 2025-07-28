'''
Project: 1
Create a python program that asks the user how far they want to travel. If they want to travel less than three miles tell them to ride Bicycle. If they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-Cycle. If they want to travel three hundred miles or more tell them to driver Super-Car.
'''
def dist_travelled(d):
    if d < 3:
        print("I suggest Bicycle to your destination.")
    elif 3 <= d < 300:
        print("I suggest Motor-Cycle to your destination.")
    else:
        print("I suggest Super-Car to your destination.")
    print("Happy Journey!")

distance = float(input("How far would you like to travel in miles?\n"))
dist_travelled(distance)
