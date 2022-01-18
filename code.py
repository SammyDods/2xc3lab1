def are_valid_groups(student_numbers, groups):
    dict = {}
    for x in student_numbers:
        dict[x] = 0
    for x in groups:
        if dict[x] == 1:
            return False
        else:
            dict[x] = 1

    return True