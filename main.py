from stats import count_words, count_characters, sort_on, sort_dictionary

def main():

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    entries = count_characters("books/frankenstein.txt")
    entries = sort_dictionary(entries)
    print(entries)
    for entry in entries:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")


main()