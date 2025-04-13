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

def move_zero(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):
        print(f"zi={zero_index} index={index}\tbefore : ",a_list, end=" ")
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
        print(f"\tafter : ", a_list)
    return(a_list)



print(move_zero([8,0,3,9,0,0,2,4, 0,5,6,]))