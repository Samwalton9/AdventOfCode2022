from helpers import load_input_as_lines


def get_elf_calories() -> list:
    tracking_list = []
    input_data = load_input_as_lines('input.txt')
    temp_list = []
    for line in input_data:
        if line != "":
            temp_list.append(int(line))
        else:
            tracking_list.append(temp_list)
            temp_list = []

    total_calorie_tracker = []
    for elf in tracking_list:
        total_calorie_tracker.append(sum(elf))

    return total_calorie_tracker


def day_1():
    calorie_list = get_elf_calories()

    print(max(calorie_list))


def day_2():
    calorie_list = get_elf_calories()
    calorie_list.sort(reverse=True)

    print(sum(calorie_list[:3]))


day_2()