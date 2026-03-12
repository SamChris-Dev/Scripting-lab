secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

while secret_number:
    num = int(input("Enter an integer: "))
    if secret_number == num:
     print(secret_number, "Well done, muggle! You are free now.")
    else:
     print("Ha ha! You are stuck in my loop!")

