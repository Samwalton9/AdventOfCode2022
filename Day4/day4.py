from helpers import load_input_as_lines


def split_string(string: str, split_char: str) -> tuple[str, str]:
    string_split = string.split(split_char)
    return string_split[0], string_split[1]


def get_range(range_string: str) -> list:
    start, end = split_string(range_string, "-")
    return list(range(int(start), int(end) + 1))


def day_1() -> None:
    input_data = load_input_as_lines()
    counter = 0
    for line in input_data:
        first_elf, second_elf = split_string(line, ",")

        first_start, first_end = split_string(first_elf, "-")
        second_start, second_end = split_string(second_elf, "-")

        first_elf_contains = int(first_start) <= int(second_start) and int(first_end) >= int(second_end)
        second_elf_contains = int(second_start) <= int(first_start) and int(second_end) >= int(first_end)

        if first_elf_contains or second_elf_contains:
            counter += 1

    print(counter)


def day_2():
    input_data = load_input_as_lines()
    counter = 0
    for line in input_data:
        first_elf, second_elf = split_string(line, ",")

        first_range = get_range(first_elf)
        second_range = get_range(second_elf)

        if any([x in second_range for x in first_range]):
            counter += 1

    print(counter)


day_1()
day_2()
