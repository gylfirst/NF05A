# TD 4 NF05A

# Exercice 1
from math import sqrt
import random as rd
from math import *


def nb_students():
    nb = int(input("Enter the number of students you have: "))
    return nb


def information(nb_students):
    list = []
    for i in range(nb_students):
        name = input("Enter the name of the sudent: ")
        grade = float(input("Enter the grade of the sudent: "))
        list.append([])
        list[i].append(name)
        list[i].append(grade)
    return list


def class_average(nb_students, list):
    sum = 0
    for i in range(nb_students):
        sum += list[i][1]
    average = sum / nb_students
    return average


def standard_deviation(average, nb_students, list):
    sum = 0
    for i in range(nb_students):
        sum += (list[i][1]-average)**2
    sum /= nb_students
    sd = sqrt(sum)
    return sd


def lowest(nb_students, list):
    min = 0
    name_min = ""
    for i in range(nb_students):
        if list[i][1] < min:
            name_min = list[i][0]
    return name_min


def highest(nb_students, list):
    max = 0
    name_max = ""
    for i in range(nb_students):
        if list[i][1] > max:
            name_max = list[i][0]
    return name_max


def rank(nb_students, list):
    condi = False
    while condi != True:
        ask_name = input("Enter the name you want to obtain the rank: ")
        for i in range(nb_students):
            if list[i][0] == ask_name:
                condi == True
                grade = list[i][1]
    grades_sorted = []
    for i in range(nb_students):
        grades_sorted.append(list[i][1])
    grades_sorted.sort(reverse=True)
    rank = grades_sorted.index(grade)
    return rank


def modify_grade(nb_students, list):
    condi = False
    ask_name = input("Enter the name you want to modify the grade: ")
    for i in range(nb_students):
        if list[i][0] == ask_name:
            modified_grade = float(input("Enter the new grade: "))
            while condi != True:
                if modify_grade >= 0 and modify_grade <= 20:
                    list[i][1] = modified_grade
                    condi = True
    return list


def menu():
    condi = False
    nb_stu = nb_students()
    list_students = information(nb_stu)
    print("\n----------------------------------\n|          Grades system         |\n|              Menu              |\n----------------------------------")
    print("1. Class Average\n2. Standard Deviation\n3. Lowest Grade\n4. Highest Grade\n5. Rank of the student\n6. Modify a grade\n7. Quit")
    print("----------------------------------\n|  Thanks for using my program   |\n----------------------------------")
    while condi != True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            ave = class_average(nb_stu, list_students)
        elif choice == 2:
            standard_deviation(ave, nb_stu, list_students)
        elif choice == 3:
            lowest(nb_stu, list_students)
        elif choice == 4:
            highest(nb_stu, list_students)
        elif choice == 5:
            rank(nb_stu, list_students)
        elif choice == 6:
            modify_grade(nb_stu, list_students)
        elif choice == 7:
            condi = True
        else:
            print("Enter a valid choice.")


menu()

# Exercice 2
s1 = input("Enter a sentence: ")
s2 = input("Enter another sentence: ")


def identical(s1, s2):
    if s1 != s2:
        print("The two sentences are not identical")
        if len(s1) > len(s2):
            print("S1 is longer than S2")
        elif len(s1) < len(s2):
            print("S2 is longer than S1")
    else:
        print("The two sentences are identical")


# Exercice 3

dic = {
    1: ('consider', 'deem to be'),
    2: ('minute', 'infitely or immeasurably small'),
    3: ('accord', 'concurrence of opinion'),
    4: ('evident', 'clearly revealed to the mind'),
    5: ('practice', 'a customary way of operation or behavior'),
    6: ('intend', 'have in mind as a purpose'),
    7: ('concern', 'something that interests you because it is important'),
    8: ('commit', 'perform an act, usually with a negative connotation'),
    9: ('issue', 'some situation or event that is thought about'),
    10: ('approach', 'move towards')
}


def random_dic(dic):
    x = rd.randint(1, len(dic))
    couple = dic.get(x)
    return couple


def info(couple):
    nb_letters = len(couple[0])
    print(f'The word contains {
          nb_letters} letters and the description is: {couple[1]}')


def game():
    cp = random_dic(dic)
    info(cp)
    word = cp[0]
    lives = 3
    for i in range(len(word)):
        condi = False
        while condi != True:
            if lives != 0:
                guess = input(f'Enter the letter number {i+1}: ')
                if guess != word[i]:
                    print("Try again!")
                    lives -= 1
                elif guess == word[i]:
                    print("You guess right!")
                    lives += 1
                    condi = True
            else:
                break
    if lives == 0:
        print("You have lost!")
    else:
        print("You have win!")
    print(f'The word was {word}.')


game()

# Exercice 4

hypotenuse = float(input("Enter the dimension of the hypothenuse: "))
leg1 = float(input("Enter the dimension of the leg 1: "))
leg2 = float(input("Enter the dimension of the leg 2: "))


def type(hyp, l1, l2):
    if hyp == l1 and hyp == l2:
        print("The triangle is equilateral")
    elif l1 == l2:
        print("The triangle is isocele")
    else:
        print("The triangle is scalene")


def area(hyp, l1, l2):
    s = hyp+l1+l2
    a = sqrt(s*(s-hyp)*(s-l1)*(s-l2))
    print(f'The area of the triangle is {a}')


def perimeter(hyp, l1, l2):
    p = hyp+l1+l2
    print(f'The perimeter is {p}')


def menu():
    condi = False
    print("\n----------------------------------\n|         Triangle system        |\n|              Menu              |\n----------------------------------")
    print("1. Type of the triangle\n2. Area of the triangle\n3. Perimeter of the triangle\n4. Quit")
    print("----------------------------------\n|  Thanks for using my program   |\n----------------------------------")
    while condi != True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            type(hypotenuse, leg1, leg2)
        elif choice == 2:
            area(hypotenuse, leg1, leg2)
        elif choice == 3:
            perimeter(hypotenuse, leg1, leg2)
        elif choice == 4:
            condi = True
        else:
            print("Enter a valid choice.")


menu()

# Exercice 5
file = open("ForestRoad PV 3kwp.csv", "rb")
print(file.readline())


def period(f):
    f.seek(79)
    start_day = f.read(2)
    f.seek(1, 1)
    start_month = f.read(2)
    f.seek(1, 1)
    start_year = f.read(4)
    print(f'{start_day}:{start_month}:{start_year}')
    return start_day


s = period(file)
s = chr(s[0]) + chr(s[1])

file.close()
