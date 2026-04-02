# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
shift_number = int(input("Enter shift number: "))

if shift_number < 1:
    print("Invalid shift")
    shift_number = int(input("Please enter a valid shift number"))


for char in text:
    if not char.isalpha():
        continue
    if char.isupper():
        code = ord(char) + shift_number
        if code == ord('Z'):
            code = ord('A') + shift_number - 1

        cipher += chr(code)
    if char.islower():
        code = ord(char) + shift_number
        if code == ord('z'):
            code = ord('a') + shift_number - 1

        cipher += chr(code)

print(cipher)
