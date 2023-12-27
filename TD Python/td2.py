# TD 2

# Exercice 1
from random import randint
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = int(input("Enter your height (in cm): "))

if len(name) > 15 and len(name) < 20:
    print("Your name is long!")
elif len(name) > 10 and len(name) <= 15:
    print("Your name is semi long!")
elif len(name) >= 8 and len(name) <= 10:
    print("Your name is semi short!")
else:
    print("Your name is short!")

if age >= 18:
    print("You are an adult!")
else:
    print("You are a child!")

if height >= 172:
    print("You are tall!")
else:
    print("You are small!")

# Exercice 2
# Question 1-2-3
nb = int(input("Enter a number: "))


def sign(n):
    if n < 0:
        print("This number is negative!")
    else:
        print("This number is positive!")


def parity(n):
    if (n % 2) == 0:
        print("This number is even!")
        return 0
    else:
        print("This number is odd!")
        return 1


def prime(n):
    cond = False
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                cond = True
                break

    if cond:
        print(n, "is not a prime number!")
        return 1
    else:
        print(n, "is a prime number!")
        return 0


sign(nb)
parity(nb)
prime(nb)

# Question 4

list = []
nb_t = int(input("Enter the number of numbers that you want to add: "))
for i in range(0, nb_t):
    nb_i = int(input("Enter a number: "))
    list.append(nb_i)


def compt_odd(list):
    compt = 0
    for element in list:
        if parity(element) == 0:
            compt += 1
    print("You have", compt, "even numbers, and",
          len(list)-compt, "odd numbers.")


compt_odd(list)


def compt_prime(list):
    compt = 0
    for element in list:
        if prime(element) == 0:
            compt += 1
    print("You have", compt, "prime numbers, and",
          len(list)-compt, "non-prime numbers.")


compt_prime(list)

# Exercice 3
# import string
# If we use the string.ascii_uppercase and string.ascii_lowercase method.

password = input("Enter your password: ")
compt_er = 0


def length(pw, cpt):
    if len(pw) < 6:
        print("Your password is too short!")
        cpt += 1
    elif len(pw) > 16:
        print("Your password is too long!")
        cpt += 1
    return cpt


def special_carac(pw, cpt):
    compt = 0
    for letter in pw:
        if letter == '#' or letter == '$' or letter == '@':
            compt += 1
    if compt < 1:
        print("Your password must contain #, $ or @.")
        cpt += 1
    return cpt


def numbers(pw, cpt):
    compt = 0
    for letter in pw:
        if letter >= '0' and letter <= '9':
            compt += 1
    if compt < 2:
        print("Your password must contain at least 2 numbers")
        cpt += 1
    return cpt


def caract(pw, cpt):
    compt = 0
    for letter in pw:
        if letter >= 'A' and letter <= 'Z':  # We can use: if letter is in string.ascii_uppercase
            compt += 1
    if compt < 2:
        print("Your password must contain at least 2 capital caracters.")
        cpt += 1
    return cpt


def caract_l(pw, cpt):
    compt_l = 0
    for letter in pw:
        if letter >= 'a' and letter <= 'z':  # We can use: if letter is in string.ascii_lowercase
            compt_l += 1
    if compt_l < 2:
        print("Your password must contain at least 2 non capital caracters.")
        cpt += 1
    return cpt


compt_er = caract_l(password, compt_er)
compt_er = caract(password, compt_er)
compt_er = numbers(password, compt_er)
compt_er = special_carac(password, compt_er)
compt_er = length(password, compt_er)

if compt_er == 0:
    print("Your password is secured!")

# Exercice 4

nb_guess = randint(0, 100)
compt = 1
nb = int(input("Enter a number: "))
while nb != nb_guess:
    if nb < nb_guess:
        print("Secret number is bigger!")
        nb = int(input("Try again! \n"))
        compt += 1
    if nb > nb_guess:
        print("Secret number is smaller!")
        nb = int(input("Try again! \n"))
        compt += 1
    if nb == nb_guess:
        print("You have found the secret number in",
              compt, "tries !\nIt was:", nb_guess)
