import os.path

def get_book_text(filepath):
    if os.path.isfile(filepath) == False:
        raise Exception("File path is invalid.")
    with open(filepath) as f:
        f = f.read()
        return f

def count_words(filepath):
    counter = 0
    text = get_book_text(filepath)
    text = text.split()
    for word in text:
        counter += 1
    return counter

def count_characters(filepath):
    text = get_book_text(filepath).lower()
    letter_count = {}
    for letter in text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def sort_on(dict):
    return dict["num"]

def sort_dictionary(dictionary):
    dict_list = []
    for k in dictionary:
        k_dict = {"char":k,"num":dictionary[k]}
        dict_list.append(k_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
