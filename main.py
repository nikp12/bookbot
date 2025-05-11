from stats import count_words, count_characters, sort_on, sort_dictionary
import os.path, sys

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    filepath = sys.argv[1]
#    if filepath == "q":
#        exit 0
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