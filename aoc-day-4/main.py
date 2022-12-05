reader = open('input.txt')
all_items = reader.read().splitlines()
reader.close()


# In how many assignment pairs does one range fully contain the other?
def part1():
    overlapping_pairs = 0
    
    for item in all_items:
        pairs = item.split(',')
        
        elf_one_nos = pairs[0].split('-')
        elf_two_nos = pairs[1].split('-')
        
        elf_one_l = int(elf_one_nos[0])
        elf_one_r = int(elf_one_nos[1])
        elf_two_l = int(elf_two_nos[0])
        elf_two_r = int(elf_two_nos[1])
        
        if (elf_one_l >= elf_two_l and elf_one_r <= elf_two_r) or \
                (elf_one_l <= elf_two_l and elf_one_r >= elf_two_r):
            overlapping_pairs += 1
    
    print(overlapping_pairs)


# 536
part1()
