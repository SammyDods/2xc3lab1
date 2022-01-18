def are_valid_groups(student_numbers, groups):
<<<<<<< HEAD
    is_in_group = [False]*len(student_numbers)
    repeating = []
    for group in groups:
        i = 0
        for student_number in student_numbers:
            if student_number in group and is_in_group[i] == True:
                repeating.append(True)
            if student_number in group and is_in_group[i] == False:
                is_in_group[i] = True
            i = i + 1
    if False in is_in_group:
        return False
    elif True in repeating:
        return False
    else: return True
=======

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

>>>>>>> 1c2d6d75140c878bcbe9510e1c88268ca7e4f53d
