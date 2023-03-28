"""My util library"""

""" input a float """
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
