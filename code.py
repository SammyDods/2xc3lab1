def are_valid_groups(student_numbers, groups):
<<<<<<< HEAD
    counter = 0 
    for student_id in student_numbers:
        for group in groups:
            for i in group:
                if i == student_id:
                    counter++1
    if counter == 1 :
        return True
    else :
        return False
=======
    dict = {}
    for x in student_numbers:
        dict[x] = 0
    for x in groups:
        y = 0
        for student in x:
            if dict[student] == 1:
                return False
            else:
                dict[student] = 1
        if y < 2 or y > 3:
            return False
    return True
>>>>>>> 300ead217ecd2284ddce799f067dbe035100c374
