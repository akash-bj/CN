def encrypt_method3(text):
    key = {
        'A':'Q','B':'W','C':'E','D':'R','E':'T','F':'Y','G':'U','H':'I','I':'O','J':'P',
        'K':'A','L':'S','M':'D','N':'F','O':'G','P':'H','Q':'J','R':'K','S':'L','T':'Z',
        'U':'X','V':'C','W':'V','X':'B','Y':'N','Z':'M'
    }

    encrypted = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted += key[char]
            else:
                encrypted += key[char.upper()].lower()
        else:
            encrypted += char
    return encrypted

def decrypt_method3(text):
    key = {
        'A':'Q','B':'W','C':'E','D':'R','E':'T','F':'Y','G':'U','H':'I','I':'O','J':'P',
        'K':'A','L':'S','M':'D','N':'F','O':'G','P':'H','Q':'J','R':'K','S':'L','T':'Z',
        'U':'X','V':'C','W':'V','X':'B','Y':'N','Z':'M'
    }

    reverse_key = {v: k for k, v in key.items()}

    decrypted = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                decrypted += reverse_key[char]
            else:
                decrypted += reverse_key[char.upper()].lower()
        else:
            decrypted += char
    return decrypted

text = input("Enter text: ")
enc = encrypt_method3(text)
print("Encrypted:", enc)
print("Decrypted:", decrypt_method3(enc))
