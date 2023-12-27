Apart1 = {
    'nb_rooms': 5,
    'total_surface': 72,
    'renewed': True,
    'furnished': False
}

Apart2 = {
    'nb_rooms': 4,
    'total_surface': 60,
    'renewed': True,
    'furnished': False
}

Apart3 = {
    'nb_rooms': 3,
    'total_surface': 38,
    'renewed': True,
    'furnished': False
}

Apart4 = {
    'nb_rooms': 1,
    'total_surface': 15,
    'renewed': False,
    'furnished': True
}

Apart5 = {
    'nb_rooms': 3,
    'total_surface': 42,
    'renewed': True,
    'furnished': False
}

Apart6 = {
    'nb_rooms': 3,
    'total_surface': 45,
    'renewed': True,
    'furnished': True
}

Apart7 = {
    'nb_rooms': 1,
    'total_surface': 16,
    'renewed': False,
    'furnished': False
}

Apart8 = {
    'nb_rooms': 2,
    'total_surface': 25,
    'renewed': True,
    'furnished': False
}

Apart9 = {
    'nb_rooms': 5,
    'total_surface': 74,
    'renewed': True,
    'furnished': False
}

Apart10 = {
    'nb_rooms': 1,
    'total_surface': 12,
    'renewed': True,
    'furnished': True
}

Apart11 = {
    'nb_rooms': 3,
    'total_surface': 35,
    'renewed': True,
    'furnished': False
}

Apart12 = {
    'nb_rooms': 4,
    'total_surface': 65,
    'renewed': False,
    'furnished': True
}

Floor1 = {
    '1': Apart1,
    '2': Apart2,
    '3': Apart3,
    '4': Apart4
}

Floor2 = {
    '1': Apart5,
    '2': Apart6,
    '3': Apart7,
    '4': Apart8
}

Floor3 = {
    '1': Apart9,
    '2': Apart10,
    '3': Apart11,
    '4': Apart12
}

List_Floor = [Floor1, Floor2, Floor3]


def average(List_Floor):
    average_surface = 0
    tot_surface = 0
    for i in range(len(List_Floor)):
        for j in range(4):
            tot_surface += List_Floor[i][str(j+1)]['total_surface']
    average_surface = round(tot_surface/12, 2)
    print(f'The average surface is: {average_surface}')


def lower_surface(List_Floor):
    min = 100
    for i in range(len(List_Floor)):
        for j in range(4):
            if (min > List_Floor[i][str(j+1)]['total_surface']):
                min = List_Floor[i][str(j+1)]['total_surface']
                floor = i+1
    print(f'The floor with the smallest apartment is: {floor} with {min}m².')


def furnished_renewed(List_Floor):
    nb_furnished = 0
    nb_renewed = 0
    for i in range(len(List_Floor)):
        for j in range(4):
            if List_Floor[i][str(j+1)]['renewed'] == True:
                nb_renewed += 1
            if List_Floor[i][str(j+1)]['furnished'] == True:
                nb_furnished += 1
    print(f'The number of renewed apartment is: {
          nb_renewed} and the number of furnished apartment is: {nb_furnished}')


def add_price(List_Floor):
    for i in range(len(List_Floor)):
        for j in range(4):
            price = float(
                input(f'Enter the price of the apartment {j+1} of floor {i+1}: '))
            List_Floor[i][str(j+1)]['price'] = price


def calcul_equi_price(List_Floor):
    for i in range(len(List_Floor)):
        for j in range(4):
            price = List_Floor[i][str(j+1)]['price']
            equi_price = 0
            max = 0
            if List_Floor[i][str(j+1)]['renewed'] == True:
                max = 2
            if List_Floor[i][str(j+1)]['furnished'] == True:
                max = 3
            if List_Floor[i][str(j+1)]['nb_rooms'] >= 5:
                max = 4
            if List_Floor[i][str(j+1)]['total_surface'] >= 150:
                max = 5
            if max == 2:
                equi_price = price*1.2
            elif max == 3:
                equi_price = price*1.3
            elif max == 4:
                equi_price = price*1.4
            elif max == 5:
                equi_price = price*1.5
            else:
                equi_price = price
            List_Floor[i][str(j+1)]['equi_price'] = equi_price
    print(List_Floor)


def store_in_file(List_Floor):
    with open("equivalent_price.txt", "w") as f:
        for i in range(len(List_Floor)):
            for j in range(4):
                eq_price = round(List_Floor[i][str(j+1)]['equi_price'], 2)
                f.write(f'The equivalent price of the apartment {
                        j+1} of the floor {i+1} is: {eq_price}\n')
    f.close()


average(List_Floor)
lower_surface(List_Floor)
furnished_renewed(List_Floor)
add_price(List_Floor)
calcul_equi_price(List_Floor)
store_in_file(List_Floor)
