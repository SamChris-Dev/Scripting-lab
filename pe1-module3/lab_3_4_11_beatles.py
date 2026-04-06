# This program creates a list of the Beatles,
#  adds some members,
#  removes some members,
#  and prints the list at each step.

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(2):
    brand_name = input("Please enter the new brand name: ")
    beatles.append(brand_name)
print("Step 3:", beatles)

# step 4
for j in range(2):
    del beatles[3]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

