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

def main():
    print(get_book_text("books/frankenstein.txt"))

count_words("books/frankenstein.txt")