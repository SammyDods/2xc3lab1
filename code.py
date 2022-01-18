def are_valid_groups(student_numbers, groups):

    dict = {}
    for x in student_numbers:
        dict[x] = 0
    for x in groups:
        y = 0
        for student in x:
            y+=1
            if dict[student] == 1:
                return False
            else:
                dict[student] = 1
        if y < 2 or y > 3:
            return False
    return True

