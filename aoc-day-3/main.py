reader = open('input.txt')
all_items = reader.read().splitlines()
reader.close()


def get_item_priority(letter):
    alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return alphabet.index(letter) + 1


# Find the item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types?
def part1():
    sum_of_priorities = 0
    
    for rucksack in all_items:
        half_length = len(rucksack) // 2
        
        compartment_one, compartment_two = rucksack[:half_length], rucksack[half_length:]
        compartment_one_set = set(compartment_one)
        compartment_two_set = set(compartment_two)
        intersection = compartment_one_set.intersection(compartment_two_set)
        
        for item in intersection:
            sum_of_priorities += get_item_priority(item)
    
    print(sum_of_priorities)


# 7795
part1()
