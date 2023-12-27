# TD 3

# Exercice 1
list = []


def create_list():
    list = []
    n = int(input("Enter the number of values you want to add in the list: "))
    for i in range(n):
        x = int(input("Enter the number: "))
        list.append(x)
    return list


def cal_list(list):
    sum = 0
    average = 0
    product = 1
    for i in range(len(list)):
        sum += list[i]
        product *= list[i]
    average = sum/len(list)
    print(f"The sum is {sum}, the average is {
          average} and the product is {product}.")


def check_in_list(list):
    x = int(input("Enter the number you want to check: "))
    if x in list:
        print(f"The number {x} is in the list.")
    else:
        print(f"The number {x} is not in the list.")


def insert(list):
    x = int(input("Enter the number you want to add: "))
    pos = int(input("Enter the position: "))
    list.insert(pos-1, x)
    return list


def remove(list):
    x = int(input("Enter the number you want to remove: "))
    if x in list:
        list.remove(x)
    else:
        print("You cannot remove a number which is not in the list!")


def cut(list):
    print((list))
    i1 = int(input("Enter the first index: "))
    i2 = int(input("Enter the second index: "))
    del list[i1:i2]
    return list


list = create_list()
cal_list(list)
check_in_list(list)
list = insert(list)
list = cut(list)

# Exercice 2
list = []


def create_list():
    list = []
    nb = int(input("How many people you want to add? "))
    for i in range(nb):
        list.append([])
        name = input("Enter the name: ")
        list[i].append(name)
        nb_ac = int(input("Enter the number of activities: "))
        for j in range(nb_ac):
            ac = input("Enter the activity: ")
            list[i].append(ac)
    # print(list)
    return list


def count_activity(list):
    nb = 0
    ac = input("Enter the activity you want to search: ")
    for i in range(len(list)):
        nb += list[i].count(ac)
    print(f"{nb} people likes {ac}.")


def mutual_activity(list):  # TO DO
    i = 0
    compt = 0
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    while list[i][0] != name1:
        i += 1
    i1 = i
    i = 0
    while list[i][0] != name2:
        i += 1
    i2 = i
    for l in range(len(list[i1])):
        for k in range(len(list[i2])):
            if list[i1][l] == list[i2][k]:
                compt += 1
    print(f"The number of mutual activities is {compt}")


def remove_activity(list):
    i = 0
    name = input("Enter the name: ")
    ac = input("Enter the activity you want to remove: ")
    while list[i][0] != name:
        i += 1
    list[i].remove(ac)
    return list


def remove_people(list):
    i = 0
    name = input("Enter the name you want to remove: ")
    while list[i][0] != name:
        i += 1
    del list[i]
    return list


def change_activity(list):
    i = 0
    name = input("Enter the name: ")
    ac = input("Enter the activity you want to replace: ")
    acn = input("Enter the new activity: ")
    while list[i][0] != name:
        i += 1
    list[i].remove(ac)
    list[i].append(acn)
    return list


list = create_list()
count_activity(list)
mutual_activity(list)
list = remove_activity(list)
list = remove_people(list)
list = change_activity(list)

# Exercice 3
dic_Lidl = {  # per kg / km
    "avocado": "2.99",
    "strawberry": "5.39",
    "banana": "1.79",
    "tomato": "3.99",
    "lemon": "1.30",
    "lettuce": "8.40",
    "quality": "good",
    "distance": "5.6"
}

dic_Casino = {  # per kg / km
    "avocado": "2.75",
    "strawberry": "4.49",
    "banana": "1.49",
    "tomato": "3.75",
    "lemon": "1.39",
    "lettuce": "7.99",
    "quality": "medium",
    "distance": "5.0"
}

dic_GrandF = {  # per kg / km
    "avocado": "2.75",
    "strawberry": "5.99",
    "banana": "2.09",
    "tomato": "3.25",
    "lemon": "3.99",
    "lettuce": "6.99",
    "quality": "good",
    "distance": "3.5"
}

dic_Carrefour = {  # per kg / km
    "avocado": "2.49",
    "strawberry": "4.99",
    "banana": "1.99",
    "tomato": "3.49",
    "lemon": "4.49",
    "lettuce": "7.99",
    "quality": "very good",
    "distance": "7.5"
}

list_of_supermarket = {
    "Lidl": {"1": "5.6", "2": "7.2"},
    "Casino": {"1": "5.0", "2": "10.8"},
    "GrandF": {"1": "3.5", "2": "4.9"},
    "Carrefour": {"1": "7.5", "2": "7.9"}
}

# weight
print("You will enter the weight of the criteria, please enter values to a total of 1")
price_w = float(input("Enter the weight of the price: "))
quality_w = float(input("Enter the weight of the quality: "))
distance_w = float(input("Enter the weight of the distance: "))
weight = price_w + quality_w + distance_w
if weight != 1.0:
    price_w /= weight
    quality_w /= weight
    distance_w /= weight
    weight = price_w+quality_w+distance_w

# search
search_vf = input("Enter the vegetable/fruit you want to know the price: ")
search = search_vf.lower()
if search in dic_Lidl:
    price_L = dic_Lidl[search]
if search in dic_Casino:
    price_C = dic_Casino[search]
if search in dic_GrandF:
    price_G = dic_GrandF[search]
if search in dic_Carrefour:
    price_Cr = dic_Carrefour[search]

print(f'Lidl:{price_L}, Casino:{price_C}, Grand Frais:{
      price_G}, Carrefour:{price_Cr}')
# sum and average price of a product
sum = float(price_L)+float(price_C)+float(price_G)+float(price_Cr)
average = sum/4
print(f'Sum: {sum}, Average: {average}')

# lower price
lowest = min(price_L, price_C, price_G, price_Cr)
if lowest == price_L:
    lowest_shop = "Lidl"
if lowest == price_C:
    lowest_shop = "Casino"
if lowest == price_G:
    lowest_shop = "Grand Frais"
if lowest == price_Cr:
    lowest_shop = "Carrefour"
print(f'Lower price for {search}: {lowest} in {lowest_shop}.')

# delete a product
choice = input("Care, you will remove a product from a shop! (y or n) ")
if choice == "y":
    remove_prod = input("Enter the product you want to remove: ")
    remove_prod.lower()
    remove_shop = input("Enter the name of the shop: ")
    remove_shop.lower()
    if remove_shop == "lidl":
        dic_Lidl.pop(remove_prod)
    if remove_shop == "casino":
        dic_Casino.pop(remove_prod)
    if remove_shop == "grand frais":
        dic_GrandF.pop(remove_prod)
    if remove_shop == "carrefour":
        dic_Carrefour.pop(remove_prod)

# better choice
if price_w > quality_w and price_w > distance_w:
    best_option = lowest_shop
if quality_w > price_w and quality_w > distance_w:
    best_option = "carrefour"
if distance_w > price_w and distance_w > quality_w:
    best_option = "grand frais"
if price_w == quality_w and price_w == distance_w:
    best_option = "casino"

print(f'The best option is: {best_option}.')

# Exercice 6
people_tuple = (['Alexis'], ['Matthieu'], ['Loan'], ['Maxence'], ['Boris'])
fav_food = ([],)
for i in range(len(people_tuple)):
    print(f'Welcome {people_tuple[i][0]}!')
    people_tuple[i].append([])
    for j in range(5):
        food = input("Enter a favorite food: ")
        people_tuple[i][1].append(food)

for i in range(len(people_tuple)):
    for j in range(5):
        food = people_tuple[i][1][j]
        fav_food[0].append(food)

search_ff = input("Enter the favorite food you want to count: ")
search = search_ff.lower()
compt = 0
for i in range(len(fav_food[0])):
    if fav_food[0][i] == search:
        compt += 1
print(f'There is {compt} people who like {search}')

if compt == 5:
    fav_list = []
    fav_list.append(search)
