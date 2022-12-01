def load_input_as_lines(file_name: str) -> list:
    input_file = open(file_name, 'r', encoding='utf-8')

    input_lines_temp = input_file.readlines()
    return [x.strip() for x in input_lines_temp]
