def shiftDec(c, n): 
    if c.isalpha(): 
        c = c.upper() 
        return chr(((ord(c) - ord('A') - n) % 26) + ord('A')) 
    else: 
        return c  
 
def dec_vigenere(ciphertext, key): 
    plain = ""
    k = 0
    for c in ciphertext:
        if c.isalpha():
            plain += shiftDec(c, key[k % len(key)])
            k += 1
        else:
            plain += c
    return plain 
 
def key_vigenere(key): 
    keyArray = [] 
    for i in range(0, len(key)): 
        keyElement = ord(key[i].upper()) - 65
        keyArray.append(keyElement) 
    return keyArray 
 
secretKey = 'DECLARATION' 
key = key_vigenere(secretKey) 
 
ciphertext = 'DNP RYR OIU OIKORO VZZIV'  
decoded = dec_vigenere(ciphertext, key) 
 
print(decoded)