#Working with even more fun list methods

x = [1, 2, 5, 9, 4, 0, 3]
y = x # Creates the list named 'y'
x.append(6)
x.append(7)
#Two new values append to the list 'x'
print(y) # But the list 'y' inherits those values
y.append('String!')
print(x) # Data Integrity FAILS

x = tuple(x) # Converts the list 'x' into a tuple, it is immutable (cannot be changed)
print(x)
print(y)


a1 = [1, 2, 3, 4]
a2 = tuple(a1)

print(a1)
print(a2)



