def key_vigenere(key): 
    keyArray = [] 
    for i in range(0, len(key)): 
        keyElement = ord(key[i].upper()) - 65 
        keyArray.append(keyElement) 
    return keyArray 
secretKey = 'DECLARATION' 
key = key_vigenere(secretKey) 
print(key)
def shiftEnc(c, n): 
    if c.isalpha(): 
        return chr(((ord(c) - ord('A') + n) % 26) + ord('A')) 
    else: 
        return c  
def enc_vigenere(plaintext, key): 
    secret = "".join([shiftEnc(plaintext[i], key[i % len(key)])  
                      if plaintext[i].isalpha() else 
plaintext[i] 
                      for i in range(len(plaintext))]) 
    return secret 
def key_vigenere(key): 
    keyArray = [] 
    for i in range(0, len(key)): 
        keyElement = ord(key[i].upper()) - 65 
        keyArray.append(keyElement) 
        return keyArray 
secretKey = 'DECLARATION' 
key = key_vigenere(secretKey) 
plaintext = 'ALL MEN ARE CREATED EQUAL' 
ciphertext = enc_vigenere(plaintext, key) 
print(ciphertext)