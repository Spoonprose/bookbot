import sys
from stats import count_words, count_characters, sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def report(file_path, word_count, dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    count = 0

    for i in dict:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
        else:
            continue
    print("============= END ===============")

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
    
    file_contents = get_book_text(file_path)
    word_count = count_words(file_contents)
    chars = count_characters(file_contents)
    dict = sort_dict(chars)
    report(file_path, word_count, dict)

main()