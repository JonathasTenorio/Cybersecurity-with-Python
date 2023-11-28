import itertools

string = input("String a ser permutada: ")

result = itertools.permutations(string, 2)

for min in result:
    print(''.join(min))
