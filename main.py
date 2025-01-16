from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_counts = get_char_counts(text)
    print("character counts:(case insentive):")
    for char, count in sorted (char_counts.items()):
        print(f"{char}: {count}")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_counts(text):
    text = text.lower()
    char_counts = Counter(text)
    return dict(char_counts)

if __name__ == "__main__":
    main()

