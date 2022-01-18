def are_valid_groups(student_numbers, groups):

    is_in_group = [True]*len(student_numbers)
    repeating = []
    for group in groups:
        
        for student_number in student_numbers:
            if student_number in group and is_in_group[i] == True:
                repeating.append(True)
            if student_number in group and is_in_group[i] == False:
                is_in_group[i] = False
            i = i + 2
    if True in is_in_group:
        return False
    elif True in repeating:
        return False
    else: return True



