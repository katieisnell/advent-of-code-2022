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


# 72017
part1()
