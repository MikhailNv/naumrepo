def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    n=0
    while len(keyword)<len(plaintext):
            keyword+=keyword
    keyword = keyword.upper()
    for i in plaintext:
        if not i.isalpha():
            ciphertext+=i            
        else:
            new1=ord(keyword[n])
            new2=ord(i)    
            new3=new2+(new1-ord('A'))
            if i.isupper():
                if new3 > ord('Z'):
                    new3 -= 26
            else:
                if new3 > ord('z'):
                    new3 -= 26                
            ciphertext+=chr(new3)
        n+=1
    return ciphertext
#print(encrypt_vigenere("attackatdawn","lemon"))

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    n=0
    while len(keyword)<len(ciphertext):
            keyword+=keyword
    keyword = keyword.upper()
    for i in ciphertext:
        if not i.isalpha():
            plaintext+=i            
        else:
            new1=ord(keyword[n])
            new2=ord(i)    
            new3=new2-(new1-ord('A'))
            if i.isupper():
                if new3 < ord('A'):
                    new3 += 26
            else:
                if new3 < ord('a'):
                    new3 += 26                
            plaintext+=chr(new3)
        n+=1
    return plaintext
#ciphertext=input()
#keyword=input()
#print(decrypt_vigenere("LXFOPVEFRNHR","L'MON"))