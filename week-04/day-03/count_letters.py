def count_letters(text_str):
    letters_dictionary = {}
    for index in range(len(text_str)):
        if not text_str[index] in letters_dictionary:
                letters_dictionary[text_str[index]] = 1
        else:
            letters_dictionary[text_str[index]] += 1
    return letters_dictionary
