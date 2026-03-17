income = float(input("Enter the annual income: "))
surplus = income - 85528

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = 14839.02 + 0.32 * surplus

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
 