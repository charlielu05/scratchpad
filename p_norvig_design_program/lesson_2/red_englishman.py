import itertools

houses = [1,2,3,4,5]
orderings = list(itertools.permutations(houses))

for (red, green, ivory, yellow, blue) in orderings:
    print(red)