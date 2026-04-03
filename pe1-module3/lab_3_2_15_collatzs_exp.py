step = 0
c = int(input("Enter a non-negative, non zero number: "))

while c != 1:
    if c % 2 == 0:
        c =  int( c / 2)
        step += 1
        print(c)
    else:
        c = 3 * c + 1
        step += 1
        print(c)

print("Step =", step)