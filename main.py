name = "Test"
price = 1.123456

# first format
print("Hello %s and price $%f is good" % (name, price))

# second format
print('Hello {:s} and price ${:f} is good'.format(name, price))
