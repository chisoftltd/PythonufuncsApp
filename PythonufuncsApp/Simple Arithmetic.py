import numpy as np

# Addition

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)

print(newarr)

# Subtraction

newarr = np.subtract(arr1, arr2)

print(newarr)

# Multiplication
newarr = np.multiply(arr1, arr2)

print(newarr)

# Division
newarr = np.divide(arr1, arr2)

print(newarr)

# Power
newarr = np.power(arr1, arr2)

print(newarr)

# Remainder
newarr = np.mod(arr1, arr2)

print(newarr)

newarr = np.remainder(arr1, arr2)

print(newarr)

# Quotient and Mod
newarr = np.divmod(arr1, arr2)

print(newarr)

# Absolute Values
arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)

print(newarr)

# Rounding Decimals
arr = np.trunc([-3.1666, 3.6667])

print(arr)

arr = np.fix([-3.1666, 3.6667])

print(arr)

# Rounding
arr = np.around(3.1666, 2)

print(arr)

# Floor
arr = np.floor([-3.1666, 3.6667])

print(arr)

# Ceil
arr = np.ceil([-3.1666, 3.6667])

print(arr)