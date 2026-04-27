# This program is a quadratic equation solver that calculates the roots of a quadratic equation given the coefficients a, b, and c.

import math as calc

a = int(input("Enter the coefficient of a : "))
b = int(input("Enter the coefficient of b : "))
c = int(input("Enter the coefficient of c : "))

x1 = (-b + calc.sqrt((b**2) - (4 * a * c)))/(2 * a)
x2 = (-b - calc.sqrt((b**2) - (4 * a * c)))/(2 * a)

print("The value of x1 and x2 from the equation (",a,"x² + ",b,"x + ",c,") is: ", sep= "")
print("x1: ", x1)
print("x2: ", x2)
