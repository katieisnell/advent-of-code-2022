reader = open('input.txt')
all_items = reader.read().splitlines()
reader.close()


def part1():
    # A = X = Rock = 1
    # B = Y = Paper = 2
    # C = Z = Scissors = 3
    total_score = 0
    
    for game in all_items:
        # A/B/C
        opponent_move = game[0]
        # X/Y/Z
        my_move = game[2]
        
        if my_move == 'X':
            total_score += 1
        elif my_move == 'Y':
            total_score += 2
        elif my_move == 'Z':
            total_score += 3
        
        if (opponent_move == 'A' and my_move == 'X') or (opponent_move == 'B' and my_move == 'Y') \
                or (opponent_move == 'C' and my_move == 'Z'):
            total_score += 3
        elif opponent_move == 'A' and my_move == 'Y':
            total_score += 6
        elif opponent_move == 'B' and my_move == 'Z':
            total_score += 6
        elif opponent_move == 'C' and my_move == 'X':
            total_score += 6
    
    return total_score


# 9241
print(part1())
