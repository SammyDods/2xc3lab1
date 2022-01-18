def are_valid_groups(student_numbers, groups):

    is_in_group = [False]*len(student_numbers)
    repeating = []
    groups_2_3 = []
    for group in groups:
        i = 0
        if len(group) >= 2 and len(group) <= 3:
            groups_2_3.append(True)
        else: groups_2_3.append(False)
        for student_number in student_numbers:
            if student_number in group and is_in_group[i] == True:
                repeating.append(True)
            if student_number in group and is_in_group[i] == False:
                is_in_group[i] = True
            i = i + 1
    if True in is_in_group:
        return False
    elif True in repeating:
        return False
    elif False in groups_2_3:
        return False       
    else: return True



