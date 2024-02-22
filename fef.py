def relation_R(x, y):
    return 4*x + y**2 >= 60

set_values = [1, 3, 5, 7, 9]

relation_pairs = [(x, y) for x in set_values for y in set_values if relation_R(x, y)]

print(relation_pairs)