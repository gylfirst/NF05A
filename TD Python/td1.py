# TD1

# Exercie 1
from math import pi
mail = "matthieu.tourrette@utt.fr"
date = "19 april 2021"

name = "Matthieu"
year = "2020-2021"
age = 19
field = "Engineer"
fav = "python"

print("Hello world,", date, mail)
print(name, year, age, field, fav)

name_in = input("Enter your name: ")
print("Hello", name_in, "Welcome to NF05A!")

# Exercice 2
a, b, c, d = 1, 2.4, "", True
print(type(a), type(b), type(c), type(d))

b_int = int(b)
a_float = float(a)
print(a_float, b_int)

b_str = str(b)
a_str = str(a)
print(a_str, b_str)

# Exercicre 3


def q1():
    a = int(input("Enter an integer: "))
    b = int(input("Enter an integer: "))

    sum = a+b
    diff = a-b
    prod = a*b
    div = a/b
    quot = a//b
    remind = a % b

    print("sum=", sum, "\ndifference=", diff, "\nproduct=", prod,
          "\ndivision=", div, "\nquotient=", quot, "\nreminder=", remind)


def q2():
    B = float(input("Enter the length B: "))
    H = float(input("Enter the height H: "))
    A = (B*H)/2
    print("The area of this triangle is:", A)


def q3():
    R = float(input("Enter the radius R: "))
    H = float(input("Enter the height H: "))
    B = pi*(R**2)
    V = (1/3)*B*H
    print("The area of the base is:", B, "and the volume of the cone is:", V)


def q4():
    a = True
    b = False
    a, b = b, a
    print("first variable =", a)
    print("second variable =", b)


q1()
q2()
q3()
q4()

# Exercice 4


def q1():
    string = str(input("Enter a string: "))
    print("The number of caracters in this string is:", len(string)-1)


def q2():
    string1 = str(input("Enter a string: "))
    string2 = str(input("Enter a string: "))
    string = string1 + string2
    print(string)


def q3():
    string = str(input("Enter a string: "))
    stringre1 = str(input("Enter a replace string: "))
    stringre2 = str(input("Enter a replace string: "))
    stringre1.replace("\n", "")
    stringre2.replace("\n", "")
    string = string.replace(stringre1, stringre2)
    print(string)


def q4():
    string = str(input("Enter a string: "))
    stringup = string.upper()
    stringdw = string.lower()
    stringtitle = string.title()
    print(stringup, stringdw, stringtitle)


def q5():
    string = str(input("Enter a string: "))
    string = string.split()
    print(string)


q1()
q2()
q3()
q4()
q5()
