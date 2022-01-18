def are_valid_groups(student_numbers, groups):

    is_in_group = [False]*2*len(student_numbers)
    repeating = []
    for group in groups:
        i = 0
        for student_number in student_number:
            if student_number in group and is_in_group[i] == True:
                repeating.append(True)
            if student_number in group and is_in_group[i] == False:
                is_in_group[i] = True
            i = i + 1
    if not True in is_in_group or not False in is_in_group:
        return False
    elif True in repeating:
        return False
    else: return True



