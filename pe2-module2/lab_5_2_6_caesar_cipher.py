# caesar cipher 
# A Caesar cipher is a simple encryption technique where each letter in the plaintext is shifted a certain number of places down the alphabet.
text = input("Enter your message: ")
cipher = ''
shift_number = int(input("Enter shift number: "))

if shift_number < 1:
    print("Invalid shift")
    shift_number = int(input("Please enter a valid shift number"))


for char in text:
    if not char.isalpha():
         cipher += char
    
    if char.isupper():
        code = ord(char) + shift_number

        if code > ord('Z'):
            code = ord(char) + shift_number -  (ord('Z') - ord('A') + 1)

        cipher += chr(code)

    if char.islower():
        code = ord(char) + shift_number

        if code > ord('z'):
            code = ord(char) + shift_number - (ord('z') - ord('a') + 1)
        cipher += chr(code)

print(cipher)
