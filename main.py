from stats import  count_words, number_of_charecters, sort_dict

import sys

def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)        

    filename = sys.argv[1]

    file_contents = get_book_text(filename)
    num_words = count_words(file_contents)
    num_char = number_of_charecters(file_contents)     
    report = sort_dict(num_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in report:
        if dictionary["char"].isalpha():
            char, num = dictionary["char"], dictionary["num"]

            print(f"{char}: {num}")
    print("============= END ===============")
    
    
main()
