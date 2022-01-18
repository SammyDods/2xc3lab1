def are_valid_groups(student_numbers, groups):

    is_in_group = [False]*len(student_numbers)
    repeating = []
    for group in groups:
        x = 1
        i = 0
        for student_number in student_numbers:
            if student_number in group and is_in_group[i] == True:
                repeating.append(True)
            if student_number in group and is_in_group[i] == False:
                is_in_group[i] = True
            i = i + 1
            x = x + 1
        if x < 2 or x > 3:
            return False
    if True in is_in_group:
        return False
    elif True in repeating:
        return False
    else: return True



