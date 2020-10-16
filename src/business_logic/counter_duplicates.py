def counter_duplicates(name):
    temp_counter = {}
    output_duplicated_counter = {}

    if not name.strip():
        return {}

    for each_letter in name:
        if not each_letter in temp_counter.keys():
            temp_counter[each_letter] = 1
        else:
            temp_counter[each_letter] = temp_counter[each_letter] + 1
            output_duplicated_counter[each_letter] = temp_counter[each_letter]

    return output_duplicated_counter