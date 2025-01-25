def sort_on(dict):
    return dict["num"]

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
        words = file_contents.split()

        words_length = len(words)
        
        letters = list(file_contents)

        letters_dict = {}

        for letter in letters:
            if letter.lower() in letters_dict:
                letters_dict[letter.lower()] += 1
            else:
                letters_dict[letter.lower()] = 1

        letters_occurance_list = []
        for char in letters_dict:
            if char.isalpha():
                letters_occurance_list.append({"letter": char, "num": letters_dict[char]})

        letters_occurance_list.sort(reverse=True, key=sort_on)

        for line in letters_occurance_list:
            print(line)
        
        
main()