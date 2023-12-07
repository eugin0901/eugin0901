characters = str(input("Enter the sequence of characters:"))

new_characters ="".join(char.lower() if char.isalpha() else "" for char in characters)
reversed_characters="".join(reversed(new_characters))

if new_characters == reversed_characters :
    print("{} is Palindrome.".format(characters))
else :
    print("{}is not Palindrom.".format(characters))









