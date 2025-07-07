from ctypes import CDLL,c_int,c_char

lib = CDLL('./calc.so') #import lib
''' Why ./calc.so?
means "look for the file in the current folder"

calc.so is your compiled C shared library
'''
def fast_calc(a,b,c):
    return lib.calculate(c_int(a),c_int(b),c_char(op.encode()))
#in py i had use ctypes to convert py val of int ,str in c data types before the calling c func
   
a = int(input("enter the the a "))
b = int(input("enter the b"))
op = input("enter operation(+,-,*,/):")

result = fast_calc(a,b,op)
print("Result:",result)



