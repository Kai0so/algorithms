def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        return False
    if high_index - low_index <= 2 and word[low_index] == word[high_index]:
        return True
    else:
        return word[low_index] == word[high_index] and is_palindrome_recursive(
            word, low_index + 1, high_index - 1
        )
