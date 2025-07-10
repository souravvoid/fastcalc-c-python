from ctypes import CDLL,c_double,c_char

lib = CDLL('./calc.so') #import lib
''' Why ./calc.so?
means "look for the file in the current folder"

calc.so is your compiled C shared library
'''
lib.calculate.restype = c_double
def fast_calc(a,b,op):
    return lib.calculate(c_double(a),c_double(b),c_char(op.encode()))
#in py i had use ctypes to convert py val of int ,str in c data types before the calling c func
   
a = float(input("enter the the a :"))
b = float(input("enter the b:"))
op = input("enter operation(+,-,*,/):")

result = fast_calc(a,b,op)
print("Result:",result)



