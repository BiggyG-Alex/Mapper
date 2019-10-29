# transposition cipher

# encryption function
def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = evenChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText


def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]  # halfLength to the end
    oddChars = cipherText[:halfLength]  # 0 to halfLength
    plaintext = ""
    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]


    return plainText

