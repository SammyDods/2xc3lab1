def are_valid_groups(student_numbers, groups):
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
