import sys
from stats import word_count, count_characters, sort_characters

def get_book_text(filepath):
    """Reads and returns the contents of a text file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    # Check for correct CLI usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        book_text = get_book_text(path)
    except FileNotFoundError:
        print(f"Error: File not found at path '{path}'")
        sys.exit(1)

    num_words = word_count(book_text)
    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
