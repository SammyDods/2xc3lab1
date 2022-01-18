def are_valid_groups(student_numbers, groups):

    Valid_Group_sizes = [2,3]
    is_in_group = [False]*len(student_numbers)
    valid_groups = []
    boolean_list1 = []
    
    for group in groups:
        i = 0
        if (len(group) in Valid_Group_sizes):
            valid_groups.append(True)
        else:
            valid_groups.append(False)
        for student_number in student_numbers:
            if student_number in group and is_in_group[i] == True:
                repeating.append(True)
            if student_number in group and is_in_group[i] == False:
                is_in_group[i] = True
            i = i + 1
    if True in is_in_group:
        return False
    elif True in boolean_list1:
        return False
    elif False in valid_groups:
        return False
    else: return True



