current_elf_calories = 0
elf_calories_array = []

with open('input.txt') as f:
    for line in f:
        if line == '\n':
            elf_calories_array.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(line)


def part1():
    elf_calories_array.sort(reverse=True)
    print(elf_calories_array[0])


def part2():
    elf_calories_array.sort(reverse=True)
    sum_of_top_3 = elf_calories_array[0] + elf_calories_array[1] + elf_calories_array[2]
    print(sum_of_top_3)


# 72017
part1()

# 212520
part2()
