def duplicate(city):
    result = list()
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2:
            result.append(city)
    return result

cities = ['Incheon', "Incheon", "Paju", "Incheon", "Seoul", "Gimpo", "Seoul"]

