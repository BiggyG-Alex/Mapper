# strings

# Concatenation
#   2 or more strings and put them together

firstName = "Blackie"
lastName = "Chan"

print(firstName + " " + lastName)

name = firstName + " " + lastName
lastFirst = lastName + ", " + firstName

print(lastFirst)

# Repetition
#   repetition operator is * it is multiplication

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + "your boat")
    print("Gently down the stream")
    print("Merrily"*4)
    print("Life is but a dream")

rowYourBoat()


# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)

middleCharIndex = len(name) // 2
print(middleCharIndex)
print(name[middleCharIndex])
print(name[-3])

for i in range(0, len(name)):
    print(name[i])

# Slicing and dicing

print(name[-4:8])

for i in range(0, len(name)+1):
    print(name[0:i])

# SEARCHING

print("Biv" in name)


if "y" not in name:
    print("y" not in name)

# Character functions

print(chr(75))
print(ord('&'))

from Mapper import *
print(LetterToindex('j'))

print(indexToLetter(44))

from Krypto import *
print(scramble2Encrypt("My favorite color is cheese"))
print(scramble2Decrypt("yfvrt oo scesM aoieclri hee"))\

