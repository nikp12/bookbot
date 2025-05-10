def get_book_text(filepath):
    with open(filepath) as f:
        f = f.read()
        return f

def main():
    print(get_book_text("books/frankenstein.txt"))

main()