import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for i in plaintext:
        if i.isalpha():
            if i.isupper():
                new1=ord(i) + shift
                if new1 > ord('Z'):
                    new1 -=26
            if i.islower():
                new1=ord(i) + shift
                if new1 > ord('z'):
                    new1 -=26
            ciphertext += chr(new1)
        else:
            ciphertext += str(i)
    print(ciphertext)
    return ciphertext
plaintext=input()
if plaintext == "":
    print()
encrypt_caesar(plaintext)

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if i.isalpha():
            if i.isupper():
                new2=ord(i) - shift
                if new2 < ord('A'):
                    new2 +=26
            if i.islower():
                new2=ord(i) - shift
                if new2 < ord('a'):
                    new2 +=26
            plaintext += chr(new2)
        else:
            plaintext += str(i)
    print(plaintext)
    return plaintext
ciphertext=input()
if ciphertext == "":
    print()
decrypt_caesar(ciphertext)



def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
