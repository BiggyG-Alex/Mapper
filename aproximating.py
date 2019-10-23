# We are learning hwo to approximate


print(22/7)
print(355/133)

import math

print(9801 / (2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(4))
print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# See the loop above. In addition to the value of pi, print the difference
# between the values calculated by the archimedes function and by math.pi.
# How many sides does it take to make the two close?


# Accumulators

acc = 0
for val in range(0, 101, 1):
    acc = acc + val


acc = 0
for even in range(0, 101, 2):
    acc = acc + even
    print(acc)

    acc = 0
    for odd in range(0, 51, 2):
        acc = acc + odd
    print(acc)

    acc = 0
    for odd in range(0, 200, 2):
        acc = acc + odd

    print(acc/100)

# Compute the sum of the first 100 even numbers
# Compute the sum of the first 50 odd numbers
# Compute the average of the first 100 odd numbers
# Write a function that returns the average of the first N numbers, where
#   N is a parameter
# Write a function called factorial that computes the product of the first N
#   numbers, where N is a parameter
# Each number in the Fibonacci sequence is the sum of the previous two numbers.
#   The first two numbers in the sequence are 1 and 1.  Compute the 10th
#   Fibonacci number.
# Write a function to compute the Nth Fibonacci number, where N is a parameter.
#   You may assume that N will be greater than
import random

print(random.random())



def montePi(numDarts):


    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi

print(montePi(10000))

import turtle


def montePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-2, -2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1,0)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()


    for i in range(numDarts):
        x = random.randrange(-100, 100) / 100
        y = random.randrange(-100, 100) / 100

        distance = math.sqrt(x ** 2 + y ** 2)
        t.goto(x, y)

        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")
        else :
            t.color("black")

        t.dot()

    pi = inCircle / numDarts * 4
    scn.exitonclick()
    return pi

print(montePi(10000))


# Assignment: modify the simulation to plot points in the entire circle
#   You will have to adjust the calculated value for pi accordingly





































































