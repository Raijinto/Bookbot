def main():
    book = "books/frankenstein.txt"
    words = get_book_text(book)
    num_words = get_num_words(words)
    letter_count = get_letter_count(words)
    list_of_dict = convert_to_dictionaries(letter_count)
    sorted = sort_list(list_of_dict)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"This book contains {num_words} words")
    for item in sorted:
        print(f"The '{item['letter']}' letter appeared {item['num']} times")
    print("--- End report ---")

def get_book_text(book):
    with open(book) as f:
        return f.read()

def get_num_words(num_words):
    return len(num_words.split())

def get_letter_count(book):
    dictionary = {}
    lower_case = book.lower()
    for letters in lower_case:
        if letters.isalpha():
            if letters in dictionary:
                dictionary[letters] += 1
            else:
                dictionary[letters] = 1
    return dictionary
    
def convert_to_dictionaries(dict):
    list_of_dict = []
    for key in dict:
        new_dict = {"letter": key, "num": dict[key]}
        list_of_dict.append(new_dict)
    return list_of_dict


def key_sort(dict):
    return dict["num"]

def sort_list(unsorted_dict):
    unsorted_dict.sort(reverse=True, key=key_sort)
    return unsorted_dict
    

main()