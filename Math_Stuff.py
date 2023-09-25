#Working with the math module and binary, hex vaules
"""
Math
"""
import math
x = 2**0.5
#print(x)

my_pi = 22/7
real_pi = math.pi

#print(my_pi)
print("The real value of pi equals",real_pi)

exp = math.pow(1.5,2) #the first value is the number, the second value is the exponent
#print(exp)

#take the square root of 49 and 50
y1 = math.sqrt(49)
y2 = math.sqrt(50)
#print(y1,y2)
"""
Binary 
"""
bin_num1 = 0b111 #Prefix the binary values with 0b
bin_num2 = 0b111011
result = bin_num1 + bin_num2 #Binary values added and then converted to base-1o value
result = bin(result) #The bin() converts a base-10 value to a binary value
#print(result)
"""
Hex
"""
hex1 = 0xfff #All hexadecimal values are prefixed with 0x
#print(hex1)

base10 = 365015
hex2 = hex(base10)
#print("The hex vaule of",base10,"equals",hex2)

binvalue = bin(base10)
#print("The binary value of", base10, "equals", binvalue)

#Controlling decimal output
real_pi = format(math.pi, ".2g")
real_pi = format(math.pi, ".4f")
print(real_pi)

