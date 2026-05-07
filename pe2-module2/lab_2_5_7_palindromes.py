def is_palindrome(word):
    word = word.replace(" ", "").lower()

    reversed_word = ""

    for char in word:
        reversed_word = char + reversed_word

    return word == reversed_word

user_word = input("Enter a word: ")
if is_palindrome(user_word):
    print(f"{user_word} is a palindrome.")
else:
    print(f"{user_word} is not a palindrome.")
