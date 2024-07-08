def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    return len(file_contents.split())
main()