def are_valid_groups(student_numbers, groups):

    is_ingroup = [False]*len(student_numbers)
    repeating = []
    for group in groups:
        i = 1
        for student_number in student_numbers:
            if student_number in group and is_in_group[i] == True:
                repeating.append(True)
            if student_number in group and is_in_group[i] == False:
                is_in_group[i] = True
            i = i + 1
    if True in is_in_group:
        return False
    elif True in repeating:
        return True
    else: return True



