BAG_SIZE = 8
POINTS = 10
ITEMS = ["в", "п", "б", "а", "и", "н", "т", "о", "ф", "д", "к", "р"]
VALUE = [25, 15, 15, 20, 5, 15, 20, 25, 15, 10, 20, 20]
AREA = [3, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 2]


def alg_bag(items, bag_size, area, value, points):
    intermediate_bag = ["и"]
    bag = [[0 for i in range(bag_size + 1)] for i in range(len(items) + 1)]
    for i in range(1, len(items)+1):
        for j in range(bag_size+1):

            if area[i-1] <= j:
                bag[i][j] = max(value[i-1]+bag[i-1][j-area[i-1]], bag[i-1][j])
            else:
                bag[i][j] = bag[i-1][j]
    bag_size_actual = bag_size
    for i in range(len(items), 0, -1):
        if bag[i][bag_size_actual] != bag[i-1][bag_size_actual]:
            for j in range(area[i-1]):
                intermediate_bag.append(items[i-1])
            bag_size_actual -= area[i-1]

    final_points = points
    for i in range(len(items)):
        if items[i] not in intermediate_bag:
            final_points -= value[i]
        else:
            final_points += value[i]
    num_of_arr = 9
    final_bag = []
    for i in range(0, len(intermediate_bag), len(intermediate_bag)//num_of_arr):
        elem_of_bag = intermediate_bag[i:i+len(intermediate_bag)//num_of_arr]
        final_bag.append(elem_of_bag)
    return final_bag, f"Итоговые очки выживания: {final_points}"


final_bag,final_points = (alg_bag(ITEMS, BAG_SIZE, AREA, VALUE, POINTS))
print(final_bag)
print(f"Итоговые очки выживани: {final_points}")
