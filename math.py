import math 

#Change module name (Can still use math alias)
import math as m

#How to import only some functions (instead of all)
from math import pi, e, sqrt, ceil, floor, pow
#--------------CONSTANTS------------------

#Prints pi
print(math.pi)

#Prints e
print(math.e)

#inf = infinity (also can be -inf (for negative infinity))
print(math.inf)
print(math.inf + 1)
print(math.inf*math.inf)

n_inf=float(-(math.inf)) #assigns neg inf to variable
print(float(-(math.inf))) #Prints negative inf
print(math.isinf(n_inf)) #Checks if n_inf is inf type and returns result

print(math.isnan(n_inf)) #Checks if Infinity is NaN (Returned False)
print(math.isnan(math.nan)) #Checks if math.nana is nan type. (Returned True)

notanumber = math.nan
print(math.isnan(notanumber)) #Checeks if notanumber variable is nan type. (Returned True)

print(math.nan==math.nan) #Is nan type equal to nan type (Retured False)
print(math.nan == notanumber) #Is nan type equal to notanumber variable

#NaN - (Not a Number) For example, a square root of a negative number is an imaginary number, therefore NAN, or 
#NaN can also be assigned to variables that do not have values and hhave yet to bbe computer
#Ifinity is NaN
#You can create NAN using floats, decminals, integers, and more
#You can check with math.isnan if a certain variable is NaN or not
#Note: We cannot use == operator to check, b/c NaN is not equal to anything! Not even itself!
print(math.nan)

#--------------Number-theoretic and representation functions------------------

#Returns number of ways to choose k item from n item without repetition and withhout order (comb n, k)
print(math.comb(6, 5))

#Rounds value upward to 4
print(math.ceil(3.4))

#Rounds value downward to 3
print(math.floor(3.6))

#Returns absolute value of the float x
print(math.fabs(-100))

#Returns factorial of x
print(math.factorial(5))

#Returns the remainder (modulo) of x/y
print(math.fmod(82, 9))

#Prints sum of between some range or an iterable
print(m.fsum(range(10))) #<--- Range count start from 9+8+7...
print(m.fsum([9,8,7,6])) #<--Iterable Interger List
print(m.fsum([3.65, 3.4, 3.0001])) #<--Iterable Floating Point List

#Returns greatest common diviser of two #s
print(math.gcd(10, 15))

"""
Returns true is values a and b are close to each other and False otherwise
  rel_tol: (The Decimal Point after both x and y - normally set to the 9th decimal point '1e-09')
    maximum difference for being considered "close", relative to themagnitude of the input values

  abs_tol:(The integar part of the distance (whole numbers))
    maximum difference for being considered "close", regardless of the magnitude of the input values\

"""
print(math.isclose(5, 10, rel_tol=1e-09, abs_tol=5.0))

#Returns the logarithm x to the given base (log base=2 of 8) (=3)
print(math.log(8, 2))

#Returns the fractional AND the decimal part of a integer or operand
print(math.modf(3.99145))

#Returns the number of permutations (combinations) without repetition in a number of items (n) and number of items to be chosen (k)
totalItems      = 6; # n
itemsToChoose   = 5;  # k
# Number of ways to choose k items from n items (without repetition and with order)
permutations = math.perm(totalItems, itemsToChoose);
print("Number of ways to choose %d items(k) from %d items(n)(without repetition & WITH order):"%(totalItems, itemsToChoose));
print(permutations);

#Power function (instead of ** aritmetic operator). Makes it more human-readable
print(math.pow(3,2))

#Testing with new module alias 
print(m.pow(3,2))

#Calculate the PRODUCT of all the elements present in the given iterable.
print(m.prod([5, 4, 3, 2, 1])) #Array
print(m.prod(range(1,6))) #Range
print(m.prod((3.2, 3.55, 9.33, -3.442))) #Tuple

#If start parameter is explicitly specified: (Multiples final product by start(3))
list=[1, 2, 3, 4, 5]
print(m.prod(list, start=3))

#If given input is empty, then method returns start value
arr=[]
tup=()
print(m.prod(tup)) #Normally, Start is 1
print(m.prod(arr, start=5)) #Specified Start value

#Returns thhe remainder of x/y
print(m.remainder(100, 24))

#How to find squareroot of a #
x = m.sqrt(25)
print(x)

#Removes the truncated (without its end section) part of a number
print(m.trunc(3.5849))

#Help/Documentation for all functions
help('math')