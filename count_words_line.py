def count_word(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            word_count = sum(len(line.split()) for line in lines)
            print("word count : ", word_count)

            letter_count = sum(len(word) for line in lines for word in line.split())
            print("letter count : ", letter)
    except FileNotFoundError:
        print(f"File {filename} not found")

count_word("sample.txt")