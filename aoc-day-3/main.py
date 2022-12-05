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


# Find the item type that corresponds to the badges of each three-Elf group.
# What is the sum of the priorities of those item types?
def part2():
    sum_of_priorities = 0
    
    i = 0
    no_of_elves = len(all_items)
    
    while i < no_of_elves:
        first_elf = all_items[i]
        second_elf = all_items[i + 1]
        third_elf = all_items[i + 2]
        
        first_elf_set = set(first_elf)
        second_elf_set = set(second_elf)
        third_elf_set = set(third_elf)
        
        intersection = first_elf_set & second_elf_set & third_elf_set
        
        for item in intersection:
            sum_of_priorities += get_item_priority(item)
        
        i += 3
    
    print(sum_of_priorities)


# 7795
part1()

# 2703
part2()
