from stats import count_words, count_characters, sort_on, sort_dictionary
import os.path

def main():
    filepath = input("Please give the relative path to the book, or enter 'q' to quit: ")
    if filepath == "q":
        quit()
    try:
        word_count = count_words(filepath)
    except Exception as e:
        print(e)
        main()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    entries = count_characters(filepath)
    entries = sort_dictionary(entries)
    for entry in entries:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")


main()