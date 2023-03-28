# classic whileloop setup

index = 1

while index <=10:
    print(index)
    index +=1 
# short hand for index = index + 1
print("Done!")    


buffer = input("Please enter a number: ")

# while buffer does not equal 
while buffer != '':
    try:
        f = float(buffer)
        print(f)
    except ValueError:
        print("That wasn't a number! Try again.")
    buffer = input("Please enter a number: ") 

print("Quit")

# Try catches the errors....except is what happens if the error occurs. 
