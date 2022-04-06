# read animals.txt
# and write animals_new.txt
old_file = open('animals.txt', 'rt')
animals = old_file.readlines()
num_animals = len(animals)
for i in range(num_animals):
    animals[i] = str.rstrip(animals[i])
old_file.close()
new_file = open('animals_new.txt', 'wt')
animal_list = animals[0]
for i in range(num_animals - 1):
    animal_list = animal_list + ' ' + animals[i + 1]

new_file.write(animal_list)
new_file.close()
