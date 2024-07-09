def main():
    book = "books/frankenstein.txt"
    words = get_book_text(book)
    num_words = get_num_words(words)
    letter_count = get_letter_count(words)
    print(f"This book contains {num_words} words")
        

def get_book_text(book):
    with open(book) as f:
        return f.read()

def get_num_words(num_words):
    return len(num_words.split())

def get_letter_count(book):
    dictionary = {}
    lower_case = book.lower()
    for letters in lower_case:
        if letters in dictionary:
            dictionary[letters] += 1
        else:
            dictionary[letters] = 1
    return dictionary

    

main()