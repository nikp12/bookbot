def get_book_text(filepath):
    with open(filepath) as f:
        f = f.read()
        return f

def count_words(filepath):
    counter = 0
    text = get_book_text(filepath)
    text = text.split()
    for word in text:
        counter += 1
    print(f"{counter} words found in the document")
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
