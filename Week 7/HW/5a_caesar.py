message = input("Enter a message to encrypt: ").upper()
key = int(input("Enter a key: "))
encrypted = ""

for letter in message:
    if letter == " ":
        encrypted += " "
    elif ord(letter) + key > ord("Z"):
        encrypted += chr(ord(letter) + key - 26)
    else:
        encrypted += chr(ord(letter) + key)

print(f"Encrypted Message: {encrypted}")