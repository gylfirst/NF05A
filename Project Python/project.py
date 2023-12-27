# initialization of the user list.
user_list = []
for i in range(26):
    user_list.append([])

# DEBUG (all # comments are for debug and """ are for doxygen doc)


def add_user(u_list):
    """
    Adds a user to Snapch'UTT
    @param u_list list of users of Snapch'UTT
    @return Returns the list with the user added

    Asks the name, age, year of study, field of study, city and the interests.
    \n And adds them to the list of users at the right place.
    """

    name = []
    fname = input("Enter the first name : ").capitalize()
    lname = input("Enter the last name : ").capitalize()
    name.append(fname)
    name.append(lname)
    age = int(input("Enter the age : "))
    year = int(input("Enter the year of study : "))
    field = input("Enter the field of study : ")
    city = input("Enter the city of residence : ")
    interests = []
    nb_interests = int(input(
        "Areas of interests : 1. sport, 2. cinema, 3. art, 4. health, 5. technology, 6. DIY, 7. cooking, 8. travel\nEnter the number of areas of interests you have : "))
    for i in range(nb_interests):
        interest = int(input(f"Enter the area of interest n°{i+1} : "))
        interests.append(interest)

    # compilation of information on the user
    user = []
    user.append(name)
    user.append(age)
    user.append(year)
    user.append(field)
    user.append(city)
    user.append(interests)

    # sorting system
    rank = ord(name[1][0])-65
    u_list[rank].append(user)
    print(f"You have successfully added {user[0][0]} {user[0][1]}")
    return u_list


def look_in_list(u_list, look_name):
    """
    Looks in the list for a user
    @param u_list list of users of Snapch'UTT
    @param look_name name of the user to search in the list
    @return Returns the emplacement of the user or 26, 0 if the user isn't found

    Takes the first letter of the family name, goes to the corresponding list.
    \n Then searches inside if it finds the name entered.
    """
    rank = ord(look_name[1][0])-65
    for i in range(len(u_list[rank])):
        if look_name == u_list[rank][i][0]:
            return i, rank
    print("\nThere is no user by this name !")
    return 26, 0


def del_user(u_list):
    """
    Deletes a user to Snapch'UTT
    @param u_list list of users of Snapch'UTT
    @return Returns the list with the user deleted

    Asks the name
    \n And adds them to the list of users at the right place
    """

    print("Caution ! You will delete a user.")

    name = []
    fname = input("Enter the first name : ").capitalize()
    lname = input("Enter the last name : ").capitalize()
    name.append(fname)
    name.append(lname)

    # look for the name in the list
    i, rank = look_in_list(user_list, name)
    if i != 26:
        del u_list[rank][i]
    print(f"You have successfully deleted {name[0]} {name[1]}")
    return u_list


def update_user(u_list):
    """
    Updates a user's information of Snapch'UTT
    @param u_list list of users of Snapch'UTT
    @return Retursn the list with the user's information updated

    Asks the name of the user to update. Asks what information the user want to update (name, age, year of study, field of study, city or the interests.
    \n And updates it in the list of users.
    """

    print("Care ! You will update a user.")
    non_name_changed = True
    name = []
    fname = input("Enter the first name : ").capitalize()
    lname = input("Enter the last name : ").capitalize()
    name.append(fname)
    name.append(lname)

    # look for the name in the list
    i, rank = look_in_list(user_list, name)
    if i != 26:
        choice = int(input(
            "What do you want to update ? (1. Name, 2. Age, 3. Year of study, 4. Field of study, 5. City of residence, 6. Interests) "))
        if choice == 1:
            new_name = []
            nfname = input("Enter the first name : ").capitalize()
            nlname = input("Enter the last name : ").capitalize()
            new_name.append(nfname)
            new_name.append(nlname)
            u_list[rank][i][0] = new_name
            # re-rank the name
            if new_name[1] != name[1]:
                new_rank = ord(new_name[1][0])-65
                updated_user = u_list[rank][i].copy()
                u_list[new_rank].append(updated_user)
                del u_list[rank][i]
                non_name_changed = False
                print(f"You have successfully updated {
                      new_name[0]} {new_name[1]}")
        elif choice == 2:
            new_age = int(input("Enter the new age : "))
            u_list[rank][i][1] = new_age
        elif choice == 3:
            new_year = int(input("Enter the new year of study : "))
            u_list[rank][i][2] = new_year
        elif choice == 4:
            new_field = int(input("Enter the new field of study : "))
            u_list[rank][i][3] = new_field
        elif choice == 5:
            new_city = input("Enter the new city of residence : ")
            u_list[rank][i][4] = new_city
        elif choice == 6:
            new_interests = []
            nb_interests = int(input(
                "Areas of interests : 1. sport, 2. cinema, 3. art, 4. health, 5. technology, 6. DIY, 7. cooking, 8. travel\nEnter the number of areas of interests you have : "))
            for j in range(nb_interests):
                interest = int(input(f"Enter the area of interest n°{j+1} : "))
                new_interests.append(interest)
            new_interests.sort()
            u_list[rank][i][5] = new_interests
        else:
            print("Wrong choice !")
    if non_name_changed:
        print(f"You have successfully updated {name[0]} {name[1]}")
    return u_list


def identify():
    """
    Identifies a user
    @return Returns the name of the user

    Asks the name of the user and returns it.
    """
    print("You need to identify yourself.")
    name = []
    fname = input("Enter your first name : ").capitalize()
    lname = input("Enter your last name : ").capitalize()
    name.append(fname)
    name.append(lname)
    return name


def follow(u_list):
    """
    Permits the user to follow another one
    @param u_list list of users of Snapch'UTT
    @return Returns the list with the user's follow

    Identifies the user, then asks the name of the person the user wants to follow
    \n And adds it to the list of follows, and creates it if there is none
    """
    name = identify()

    # look for the name in the list
    i, rank = look_in_list(user_list, name)
    if i != 26:
        # if the follow section doesn't exist
        if len(u_list[rank][i]) == 6:
            u_list[rank][i].append([])
        print(
            f'Welcome {name[0]}, please enter the name of the person you want to follow.')
        fname = []
        ffname = input("Enter the first name : ").capitalize()
        flname = input("Enter the last name : ").capitalize()
        fname.append(ffname)
        fname.append(flname)
        u_list[rank][i][6].append(fname)

    print(f"You have successfully followed {fname[0]} {fname[1]}")
    return u_list


def display_follows(u_list):
    """
    Displays the follows of the user
    @param u_list list of users of Snapch'UTT

    Identifies the user and prints the different follows, or none if there is none.
    """
    name = identify()
    i, rank = look_in_list(user_list, name)
    if i != 26:
        if len(u_list[rank][i]) == 6:
            print("\nYou do not follow anyone !")
        else:
            for j in range(len(u_list[rank][i][6])):
                print(f'You are following {u_list[rank][i][6][j][0]} {
                      u_list[rank][i][6][j][1]}.')


def search(u_list):
    """
    Searches a user by name, interests, year and field of study
    @param u_list list of users of Snapch'UTT

    Asks something to search. Searches if a name, interest, year of study, field of study corresponds.
    \n If it does, print the name of the user. Print the number of results.
    """
    print("You can search by name, field, year of study and area of interests (with the numeros : 1. sport, 2. cinema, 3. art, 4. health, 5. technology, 6. DIY, 7. cooking, 8. travel)")
    input_search = input("Enter something to search : ")
    print("Results :")
    cpt = 0
    for i in u_list:
        for j in i:
            if input_search == j[0][0]:     # first name
                print(j[0][0], j[0][1])
                cpt += 1
            if input_search == j[0][1]:     # last name
                print(j[0][0], j[0][1])
                cpt += 1
            if input_search == j[3]:        # field
                print(j[0][0], j[0][1])
                cpt += 1
            if int(input_search) == j[2]:        # yos
                print(j[0][0], j[0][1])
                cpt += 1
            for k in j[5]:                  # interests
                if int(input_search) == k:
                    print(j[0][0], j[0][1])
                    cpt += 1
    if cpt == 0:
        print("\nThere are no results")
    elif cpt == 1:
        print("\nThere is 1 result")
    else:
        print(f"\nThere are {cpt} results")


def suggestions(u_list):
    """
    Displays a list of maximum 5 suggestions for the user to follow
    @param u_list list of users of Snapch'UTT

    Identifies the user, then copies the list of interests and follows
    \n For mutual interests: gets the others' interests and compares it with the user
    \n If a user has the same interests as the logged in, it will add the name to the list
    \n If not, it will rank the users depending of the number of mutual interests
    \n\n For mutual contacts: gets the follows of the current follows of the user
    \n If the user is in the follows list, the function will remove it.
    \n It counts the number of occurence of the different names, in order to class it by maximum
    \n If one of the list is empty, the suggestions are the names in the other list
    \n Otherwise, it will add the names present in the two lists
    \n Then, it prints the final suggestions
    """
    name = identify()
    sugg = []
    sugg_interests = []
    sugg_contact = []
    followersfl = []

    # look for the name in the list
    rank = ord(name[1][0])-65
    for i in range(len(u_list[rank])):
        if name == u_list[rank][i][0]:
            interests = u_list[rank][i][5].copy()
            rank_index = i
            if len(u_list[rank][i]) == 7:
                followers = u_list[rank][i][6].copy()
                for n in range(len(followers)):
                    rankf = ord(followers[n][1][0])-65
                    for j in range(len(u_list[rankf])):
                        if len(u_list[rankf][j]) == 7:
                            followersl = u_list[rankf][j][6].copy()
                            followersfl.append(followersl)
    # print(followersfl)

    # get others' interests
    other_interests = []
    names = []
    names_i = []
    for i in range(len(u_list)):
        for j in range(len(u_list[i])):
            if i != rank:
                other_interests.append(u_list[i][j][5])
                names.append(u_list[i][j][0])
    # print(other_interests)
    # print(names)

    # if they have the same interests as the user
    for i in range(len(other_interests)):
        if other_interests[i] == interests:
            sugg_interests.append(names[i])

    for i in interests:
        for j in range(len(other_interests)):
            for k in range(len(other_interests[j])):
                if i == other_interests[j][k]:
                    names_i.append(names[j])
    # print(names_i)

    c_list = []
    for i in names:
        count = names_i.count(i)
        c_list.append(count)

    for i in range(len(names)-len(sugg_interests)):
        maxi = 0
        maxi = max(c_list)
        max_index = c_list.index(maxi)
        if len(u_list[rank][rank_index]) == 7:
            if names[max_index] not in u_list[rank][rank_index][6]:
                sugg_interests.append(names[max_index])
                del names[max_index]
                del c_list[max_index]
        else:
            sugg_interests.append(names[max_index])
            del names[max_index]
            del c_list[max_index]
    # print(sugg_interests)

    # removing identify name in the potential suggestions
    i_l = []
    j_l = []
    for i in range(len(followersfl)):
        for j in range(len(followersfl[i])):
            if followersfl[i][j] == name:
                i_l.append(i)
                j_l.append(j)
    for i in range(len(i_l)):
        del followersfl[i_l[i]][j_l[i]]
    # print(followersfl)

    # decompiling the list
    flist = []
    for i in range(len(followersfl)):
        for j in range(len(followersfl[i])):
            name_follow = followersfl[i][j]
            flist.append(name_follow)
    # print(flist)

    # count
    uflist = []
    count_list = []
    for i in flist:
        if i not in uflist:
            uflist.append(i)
    for i in uflist:
        count = 0
        count += flist.count(i)
        count_list.append(count)
    # print(uflist,";", count_list)

    # looking for max count
    for i in range(len(uflist)):
        maxi = 0
        maxi = max(count_list)
        max_index = count_list.index(maxi)
        if len(u_list[rank][rank_index]) == 7:
            if uflist[max_index] not in u_list[rank][rank_index][6]:
                sugg_contact.append(uflist[max_index])
                del uflist[max_index]
                del count_list[max_index]
    # print(sugg_contact)

    # comparaison between interests and contacts
    x = 0
    if len(sugg_contact) == 0:
        for i in sugg_interests:
            if x != 5:
                sugg.append(i)
                x += 1
    elif len(sugg_interests) == 0:
        for i in sugg_contact:
            if x != 5:
                sugg.append(i)
                x += 1
    else:
        for i in sugg_interests:
            if i in sugg_contact and x != 5:
                sugg.append(i)
                x += 1

    # print of suggestions
    if len(sugg) == 0:
        print("There is no suggestion")
    else:
        for i in sugg:
            print(f'Your suggestion: {i[0]} {i[1]}')


print("Welcome to Snapch'UTT !")
while True:
    print("\n")
    print("Choose one of the following options by entering the corresponding number:")
    print("1 - Add a user")
    print("2 - Delete a user")
    print("3 - Update a user's information")
    print("4 - Follow a user")
    print("5 - Display the follows of a user")
    print("6 - Search a user by name, field, year of study and area of interest")
    print("7 - User suggestions to follow")
    print("8 - Close Snapch'UTT")
    print("Enter the number corresponding to your choice:")
    choice = input()
    if choice == '1':
        user_list = add_user(user_list)
    elif choice == '2':
        user_list = del_user(user_list)
    elif choice == '3':
        user_list = update_user(user_list)
    elif choice == '4':
        user_list = follow(user_list)
    elif choice == '5':
        display_follows(user_list)
    elif choice == '6':
        search(user_list)
    elif choice == '7':
        suggestions(user_list)
    elif choice == '8':
        break
    else:
        print("It's not a valid number!")
