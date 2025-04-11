import sys

from stats import get_num_words
from stats import get_num_characters
from stats import sort_characters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as book:
        book_text = book.read()
    return book_text

def main():
    book = get_book_text(sys.argv[1])
    num_words = get_num_words(book)
    sorted_characters = sort_characters(get_num_characters(book))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------") 
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_characters:
        print(f"{dictionary['character']}: {dictionary['value']}")
    print("============= END ===============")

main()