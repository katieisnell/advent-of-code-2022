import numpy as np
import re

reader = open('input.txt')
all_items = reader.read().splitlines()
reader.close()


# After the rearrangement procedure completes, what crate ends up on top of each stack?
def part1():
    crate1 = ['Z', 'P', 'M', 'H', 'R']
    crate2 = ['P', 'C', 'J', 'B']
    crate3 = ['S', 'N', 'H', 'G', 'L', 'C', 'D']
    crate4 = ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L']
    crate5 = ['F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M']
    crate6 = ['T', 'F', 'S', 'Z', 'B', 'G']
    crate7 = ['N', 'R', 'V']
    crate8 = ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M']
    crate9 = ['W', 'Q', 'N', 'J', 'F', 'M', 'L']
    
    crates = np.array([crate1, crate2, crate3, crate4, crate5, crate6, crate7, crate8, crate9])
    
    for step in all_items:
        move_no_match = re.search('move (\d+)', step)
        move_no = int(move_no_match.group(1))
        from_stack_match = re.search('from (\d+)', step)
        from_no = int(from_stack_match.group(1))
        to_stack_match = re.search('to (\d+)', step)
        to_no = int(to_stack_match.group(1))
        
        from_index = from_no - 1
        to_index = to_no - 1
        
        current_move_no = move_no
        while current_move_no > 0:
            popped_item = crates[from_index].pop()
            crates[to_index].append(popped_item)
            current_move_no = current_move_no - 1
    
    top_of_crates = ''
    for crate in crates:
        top_of_crates = top_of_crates + crate.pop()
    
    print(top_of_crates)


# VQZNJMWTR
part1()
