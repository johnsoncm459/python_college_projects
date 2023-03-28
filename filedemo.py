
# variable with open "testdata.txt" file and w for write....put r if just read
#myfile = open('testdata.txt', 'w')

#msg_out = "This is my first write to disk\n"
#x = 7 
# put str(x) to convert int to a string
#myfile.write('Hello disk world!\n')
#myfile.write(msg_out)
#myfile.write(str(x))

#myfile.close()

myfile = open('testdata.txt', 'r')

# strip function removes white space

#for line in myfile:
    #line = line.strip() 
    #print(line)

# the print statement adds a line plus the line we added so double spaced

#myfile.close()

#myfile = open('testdata.txt', 'r')

#line_1 = myfile.readline()
#line_2 = myfile.readline()
#x_1 = int(myfile.readline())

#myfile.close()

#print(line_1.strip())
#print(line_2strip())
#print(x_1)

# While loop

#myfile = open('testdata.txt', 'r')

#line = myfile.readline()
#while line != '':
  #  print(line.strip())
# line = myfile.readline()

#myfile.close()

# how to open and close a file without myfile.close()
with open('testdata.txt', 'r') as myfile:
    for line in myfile:
        line = line.strip()
        print(line)
