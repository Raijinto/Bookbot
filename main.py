def main():
    book = "books/frankenstein.txt"
    words = get_book_text(book)
    num_words = get_num_words(words)
    print(f"This book contains {num_words} words")
        

def get_book_text(book):
    with open(book) as f:
        return f.read()

def get_num_words(word_count):
    return len(word_count.split())

main()