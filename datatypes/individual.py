#integers range from 0 to infinity to -infinity
x = 1
print(type(x))
y = 2
# print(type(y))
# print(x + y)
# print(type(x + y))
#arithmetic operations
# add = x + y #3
# sub = x - y #-1
# div = x/y #.5
# mul = x * y #2
#
# print(add, sub, div, mul)
#
# mod = 5 % x #0
# print(mod)
#
# floordiv = 105 // 10 #10
# print(floordiv)
#
# dm = divmod(115, 10)
# print(dm)
#
# a = -5
# print(type(a))
#
# print(abs(a))
# print(abs(x))
#
#displays the attributes that can be performed on a datatype
# print(dir(x))
# print(dir(int))
#creating integers
# i = 10
# r = int(100)
# print(r)
# r = int(0.5)
# print(r)
# r = int(-5)
# print(r)
# x = int()
# print(x)
# #float is integers with decimal point or decimal values 0.0 to infinity to -infinity
# f = 0.5
# print(type(f))
# f = float(0)
# print(f)
# f = float(10.0)
# print(f)
# f = float(-1.5)
# print(f)
# print(abs(f))

# 0.1 - 0.4 => 0 1.4, 1 , 1+0
# 0.5 - 0.9 => 1 1.5, 2 , 1 + 1

# print(round(1.5))
# print(round(1.4))
# print(round(1.45))
# print(round(0.56))
# print(round(0.46))
# print(round(0.56, 1))
# print(round(0.46, 1))
# print(round(0.462, 2))
# print(round(1.562, 3))

# x = 1.5
# print(round(1.55, 1))    #.1 - .4 =>0   .5 - .9 => 1 1.5=> 1 + 1 = 2, 1.4 => 1 + 0 = 1
# x = 2.456
# print(round(x, 2))
# import math #math is a module or library
# print(math.trunc(x)) #removes decimal values
# print(math.trunc(2.56))
# print(math.trunc(-1.101))

#complex real value and imaginary part default value 0+0j or 0j
# x = 1+2j
# y = complex()
# print(y)
# c = complex(2, 2)
# print(c)
# v = complex(-2)
# print(v)
# b = complex(2, -2)
# print(b)
# t = complex(3.2, 5.4)
# print(t)
# j = complex(real=0, imag=45)
# print(j)
# add = x + c #3 + 4j
# sub = x - c #-1 + 0j
# div = c / x #1.2-0.4j => 2+1j
# mul = x * c #-2 + 6j => 2+4j
# # dm = divmod(x, c) TypeError: can't take floor or mod of complex number.
# print(add, sub, mul, div)

#boolean it will be having only True or False by default it will be false
# v = True
# print(v)
# b = False
# print(type(b))
# d = bool()
# print(d)
# a = bool(5)
# print(a)
# b = bool(0)
# print(b)
# n = bool(-2)
# print(n)
#arithmetic operations True = 1 False = 0
# add = True + False #true => 1
# sub = True - False #true => 1
# mul = True * False #false => 0
# div = False / True #0.0
# print(add, sub, mul, div)

x = 100
y = 10

print(x / y)
print(x % y)
print(x // y)
print(abs(-5))
print(abs(+5))

print(y ** 100)
print(y * y * y )
print(y ** y ** y)

