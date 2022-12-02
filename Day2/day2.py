from helpers import load_input_as_lines

# Mapping rock, paper, and scissor strings
shapes_map = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

# Keys are played, value is what it beats
beat_map = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}


# As above, but for losing
lose_map = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}


shape_score = {
    'A': 1,
    'B': 2,
    'C': 3
}


def determine_score(mine: str, theirs: str) -> int:
    score = 0
    if beat_map[mine] == theirs:
        score += 6
    elif mine == theirs:
        score += 3
    else:
        score += 0

    score += shape_score[mine]

    return score


def day_1():
    input_list = load_input_as_lines()
    total_score = 0
    for line in input_list:
        score = determine_score(shapes_map[line[-1]], line[0])
        total_score += score

    print(total_score)


def day_2():
    input_list = load_input_as_lines()
    total_score = 0
    for line in input_list:
        status = line[-1]
        theirs = line[0]
        if status == 'X':
            # lose
            score = determine_score(beat_map[theirs], theirs)
        elif status == 'Y':
            # draw
            score = determine_score(theirs, theirs)
        else:
            # win
            score = determine_score(lose_map[theirs], theirs)
        total_score += score

    print(total_score)


day_1()
day_2()
