Dell = {
    'memory': 8,
    'nb_cores': 8,
    'screen_size': 13,
    'price': 699
}

Toshiba = {
    'memory': 12,
    'nb_cores': 16,
    'screen_size': 17,
    'price': 999
}

HP = {
    'memory': 16,
    'nb_cores': 24,
    'screen_size': 17,
    'price': 1399
}

computers = {
    '1': Dell,
    '2': Toshiba,
    '3': HP
}


def average_size(cp):
    total = 0
    average = 0
    for k, v in cp.items():
        total += v['screen_size']
    average = round(total/3, 2)
    print(f'The average screen size is: {average}')


def best_prize(cp):
    best = 99999
    model = 0
    for k, v in cp.items():
        if v['price'] < best:
            best = v['price']
            model = k
    print(f'The cheapest computer is: {model} at {best}€')


def calcul_quality(cp):
    for k, v in cp.items():
        q = 2*v['nb_cores'] + 3*v['memory'] + \
            1.5*v['screen_size'] - v['price']/100
        v['quality'] = q
    bestq = 0
    model = 0
    for k, v in cp.items():
        if v['quality'] > bestq:
            bestq = v['quality']
            model = k
    print(f'The best quality is: {bestq} for the computer {model}')


def add_feature(cp):
    name = input("Enter the name of a new feature: ")
    for k, v in cp.items():
        value = float(input("Enter the value of this feature: "))
        v[name] = value


def recalcul_quality(cp):
    for k, v in cp.items():
        coeff = float(input("Enter the coefficient c<1: "))
        q = 2*v['nb_cores'] + 3*v['memory'] + \
            1.5*v['screen_size'] - v['price']/100
        v['re_quality'] = q*coeff
    bestq = 0
    model = 0
    for k, v in cp.items():
        if v['re_quality'] > bestq:
            bestq = v['re_quality']
            model = k
    print(f'The best quality is: {bestq} for the computer {model}')


average_size(computers)
best_prize(computers)
calcul_quality(computers)
add_feature(computers)
recalcul_quality(computers)
