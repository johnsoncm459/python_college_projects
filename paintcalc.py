import math

from util import input_float

AREA_PER_DOOR = 14.0
AREA_PER_WINDOW = 8.5
AREA_PER_GALLON = 350

#Creating a function
def input_float(prompt):
    done = False
    while not done:
        try:
            buffer = input(prompt)
            value = float(buffer)
            done = True
        except ValueError:
            print("Invalid input, please try again.")
    return value



# get wall measurements and calc the area
wall_length = input_float("Please enter the wall length: ")
wall_height = input_float("Please enter the wall height: ")
wall_area = wall_length * wall_height

# deal with doors
door_count = int(input("Please enter the number of doors: "))
door_allowance = door_count * AREA_PER_DOOR

# deal with windows
window_count = int(input("Please enter the number of windows: "))
window_allowance = window_count * AREA_PER_WINDOW

# figure of the actual area to paint
total_area = wall_area - door_allowance - window_allowance

# calc gallons needed. NOTE: Always round up
gallons = total_area / AREA_PER_GALLON
gallons = math.ceil(gallons)

# figure price
paint_price = input_float("Please enter price of paint per gallon: ")
cost = gallons * paint_price

# display results
print("Gallons needed is {0}".format(gallons))
print("Total cost is ${0:.2f}".format(cost))
