# Converting Num to Bin

dec_num = int(input("Enter a Base10 number:"))
binary_rep = bin(dec_num)[2:] # The [2:] gets rid of the 0b, which tells it is binary
print(binary_rep)

length = len(binary_rep) #Checking to make sure it is 8-bit
print(length)

