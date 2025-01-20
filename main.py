def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_counts(dict):
    counts = []
    for k in dict:
        item = {}
        if k.isalpha():
            item['name'] = k
            item['num'] = dict[k]
            counts.append(item)

    def sort_on(dict):
        return dict["num"]

    counts.sort(reverse=True, key=sort_on)
    return counts

def print_report(path):
    print(f"--- Begin report of {path} ---")
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()

    word_count = get_word_count(file_contents)
    print(f"{word_count} words found in the document")
    print("")
    
    char_count = get_char_count(file_contents)
    sorted_counts = sort_counts(char_count)

    for dict in sorted_counts:
        char = dict['name']
        count = dict['num']
        print(f"The '{char}' character was found {count} times ")
    
    print("--- End report ---")
    



def main():
    file_path = 'books/frankenstein.txt'
    print_report(file_path)

main()

