# Simple program that prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum"
# prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
#  prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.


String = input("Please enter your string: ")


if (String == "Spathiphyllum"):
    print("Yes - Spathiphyllum is the best plant ever!")
elif (String == "spathiphyllum"):
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not ", String, "!", sep="")
