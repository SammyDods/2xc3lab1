def are_valid_groups(student_numbers, groups):

    is_in_group = [True]*len(student_numbers)
    repeating = []
    for group in groups:

        x = 1
        i = 0
        
                is_in_group[i] = True
            i = i + 1
            x = x + 1
        if x < 2 or x > 3:
            return False



