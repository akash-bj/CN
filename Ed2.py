def encrypt_method2(text):
    count = {}
    encrypted = ""
    shifts_used = []

    for char in text:
        if char.isalpha():
            c = char.lower()
            if c not in count:
                count[c] = 1
                shift = 3
            else:
                count[c] += 1
                shift = 3 + (count[c] - 1) * 2

            start = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)

            encrypted += encrypted_char
            shifts_used.append(shift)
        else:
            encrypted += char
            shifts_used.append(0)

    return encrypted, shifts_used

def decrypt_method2(text, shifts):
    decrypted = ""
    for i, char in enumerate(text):
        if char.isalpha():
            shift = shifts[i]
            start = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - start - shift) % 26 + start)
        else:
            decrypted += char
    return decrypted

text = input("Enter text: ")
enc, shifts = encrypt_method2(text)
print("Encrypted:", enc)
dec = decrypt_method2(enc, shifts)
print("Decrypted:", dec)
