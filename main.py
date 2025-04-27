import os, sys

def find_books(folder):
    filepaths = []
    directory = os.scandir(folder)
    for file in directory:
        filename = file.path
        if filename.endswith(".txt"):
            filepaths.append(filename)
    return filepaths

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)

from stats import get_num_words, get_letter_stats, create_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>/<path_to_books_folder>")
        sys.exit(1)
    else:
        try:
            books = []
            if os.path.isdir(sys.argv[1]):
                books = find_books(sys.argv[1])
            else:
                books.append(sys.argv[1])
            for book in books:
                book_text = get_book_text(book)
                print("============ BOOKBOT ============")
                print(f"Analyzing book found at {book}...")
                print("----------- Word Count ----------")
                print(f"Found {get_num_words(book_text)} total words")
                print("--------- Character Count -------")
                character_report = create_report(get_letter_stats(book_text))
                for k in character_report:
                    print(f'{k["char"]}: {k["num"]}')
                print("============= END ===============")
        except FileNotFoundError as not_found:
            print(f"'{not_found.filename}' could not be opened (make sure it exists)")
        except Exception as e:
            print(e)

main()
