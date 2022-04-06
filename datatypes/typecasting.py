#typecasting converting another data into required data
x = int()
y = float()
z = complex()
a = bool()
# print(x, y, z, a)
#
# x = int(1.5) #converting a float to integer
# print(x)
# x = int(2+2j) #TypeError: can't convert complex to int because its having imaginary
# print(x)
# x = int(True) #converting boolean to integer
# print(x)

y = float(2) #converting a integer to float
# y = float(2 + 2j) #TypeError: can't convert complex to float because its having imaginary
y = float(False) #converting boolean into float
# print(y)

z = complex(1) #converting a integer to complex
z = complex(1,2)
z = complex(1.5) #converting float to complex
z = complex(True, True) #converting boolean to complex
z = complex(1+2j)
# print(z)

a = bool(5) #converting a integer to boolean
a = bool(2.5) #converting float to boolean
a = bool(1+2j) #converting complex to boolean
a = bool(0j)
a = bool(True)
a = bool(False)
# print(a)
#bool() is not converting it is checking whether value is there or not


