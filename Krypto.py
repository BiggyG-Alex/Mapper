# transposition cipher

# encryption function


def scramble2Encrypt(plainText):
    # stripSpaces(plainText)
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText


def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]  # halflength to the end
    oddChars = cipherText[:halfLength]   # 0 to halflength - 1
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText

# write a caesarEncrypt(plainText, shift)
# write a caesarDecrypt(cipherText, shift)

def ceasarEncrypt(plainText, shift):

    cipher = ' '
    for char in plainText:
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher

plainText = input("enter string: ")
A = int(input("enter shift number: "))
print("original string: ", plainText)
print("after encryption: ", ceasarEncrypt(plainText, A))



def ceasarDecrypt(cipher)



