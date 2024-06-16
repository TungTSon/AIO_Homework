def count_chars(word):
    letter_count = {}
    for char in word:
        char = char.lower()  # Convert to lowercase to handle both uppercase and lowercase uniformly
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count


if __name__ == "__main__":
    input_word = input("Enter a word: ")
    result = count_chars(input_word)
    print(result)
