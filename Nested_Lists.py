# Working with nested Lists

number_sequence = [
    0, 1, 2, 3
]

print(number_sequence)

# Nested_num_list is an example of a nested list or a list within a list
nested_num_list = [
    [1, 2, 3], # Index position 0
    [4, 5, 6], # Index position 1
    [7, 8, 9], # Index position 2
    [0]
]
print(nested_num_list[1])
# The interpreter treats nested lists in a row column first, column second order
print(nested_num_list[1][2])

for i in nested_num_list: # This passes each nested list to i
    for j in i: # This passes each individual item in each list to j
        print(j)

good_nested_list = [
    ['a', 'b'],
    ['z', 's', 'w'],
    ['q', 'e'],
]

better_list = []
for i in good_nested_list:
    for j in i:
        better_list.append(j)

    better_list.sort()
    print(better_list)


