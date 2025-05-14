import sys
from stats import (
        count_words, 
        count_chars,
        sorted_chars
)

def get_book_text(path_to_file):
        with open(path_to_file) as f:
                file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    count = count_words(text)
    letters = count_chars(text)
    letter_sort = sorted_chars(letters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", sys.argv[1], "...")
    print("----------- Word Count ----------")
    print("Found", count, "total words")
    print("--------- Character Count -------")
    for item in letter_sort:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
