def encrypt(text, key_a, key_b):
    result = ""
    for char in text.upper():
        if char.isalpha():

            x = ord(char) - 65 
            
            y = (key_a * x + key_b) % 26
        
            result += chr(y + 65)
        else:
            result += char 
    return result

plain = "HELLO"
key_a = 5
key_b = 8

cipher = encrypt(plain, key_a, key_b)
print("Original:", plain)
print("Encrypted:", cipher)
def decrypt(cipher_text, key_a, key_b):
    result = ""
    
    inverse_a = 0
    for i in range(1, 26):
        if (key_a * i) % 26 == 1:
            inverse_a = i
            break
            
    if inverse_a == 0:
        return "Error: Yeh Key A decrypt nahi ho sakti!"

    for char in cipher_text.upper():
        if char.isalpha():

            y = ord(char) - 65

            x = (inverse_a * (y - key_b)) % 26

            result += chr(x + 65)
        else:
            result += char
            
    return result

cipher = "RCLLA" 
key_a = 5
key_b = 8

original = decrypt(cipher, key_a, key_b)
print("Cipher Text:", cipher)
print("Decrypted Text:", original)