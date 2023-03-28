print("Start")

# cumulative has to be there to provide a variable / so it starts at zero and then loops below the for action
total = 0

# Colon has to be on the end / augmented operator += x
for x in range(1,11):
    #total = total + x
    total += x
    print(x, total)

print("End")

# Comment out by ctrl + / 

# namelist = ['Ed', 'Ken', 'Jeff', 'Taylor']
# for name in namelist: 
#     print(name)

# pricelist = [.79,1.25,100,1999.95]

# # formatting %0.2f both versions will work / bottom is preferred / the ten is spaces / greater than sign moves everything over
# for price in pricelist:
#     # print("price is $%0.2f" % price)
#     # print("price is ${0:10.2f}".format(price))
#     price_fmt = "$" + "{0:.2f}".format(price)
#     msg = "prive is {0:>10}".format(price)
#     print(msg)
# # Long version what each thing is doing
