def is_anagram(first_string, second_string):
    first_string_list = list(first_string.lower())
    second_string_list = list(second_string.lower())

    sort_string(first_string_list)
    sort_string(second_string_list)

    first_string = "".join(first_string_list)
    second_string = "".join(second_string_list)

    if not first_string or not second_string:
        string_is_anagram = False
    elif first_string == second_string:
        string_is_anagram = True
    else:
        string_is_anagram = False
    return (first_string, second_string, string_is_anagram)


def sort_string(string_list, start=0, end=None):
    if end is None:
        end = len(string_list)
    if (end - start) > 1:
        mid = (start + end) // 2
        sort_string(string_list, start, mid)
        sort_string(string_list, mid, end)
        merge(string_list, start, mid, end)


def merge(string_list, start, mid, end):
    left = string_list[start:mid]
    right = string_list[mid:end]
    left_index, right_index = 0, 0

    for index in range(start, end):
        if left_index >= len(left):
            string_list[index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            string_list[index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            string_list[index] = left[left_index]
            left_index = left_index + 1
        else:
            string_list[index] = right[right_index]
            right_index = right_index + 1
