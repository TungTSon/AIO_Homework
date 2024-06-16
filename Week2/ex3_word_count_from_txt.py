def word_count(file_path):
    # Read the file
    with open(file_path, 'r') as f:
        text = f.read()

    # Convert all split words to lowercase
    word_list = [word.lower() for word in text.split()]
    word_count_list = {}    # create an empty dictionary first: to count word
    for word in word_list:
        word_count_list[word] = word_list.count(word)

    # Print the resulting dictionary
    for word, count in word_count_list.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    file_path = r"./P1_data.txt"
    word_count(file_path)
