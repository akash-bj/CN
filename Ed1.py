def encrypt_method1(text):
    encrypted = ""
    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - start + 3) % 26 + start)
        else:
            encrypted += char
    return encrypted

def decrypt_method1(text):
    decrypted = ""
    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - start - 3) % 26 + start)
        else:
            decrypted += char
    return decrypted

text = input("Enter text: ")
enc = encrypt_method1(text)
print("Encrypted:", enc)
print("Decrypted:", decrypt_method1(enc))
