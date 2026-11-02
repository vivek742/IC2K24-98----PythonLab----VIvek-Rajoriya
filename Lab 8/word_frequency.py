# Word Frequency Counter


def clean_text(text):
    text = text.lower()
    clean = ""
    for character in text:
        if character.isalnum() or character.isspace():
            clean += character
        else:
            clean += " "
    return clean


def count_words(text):
    counts = {}
    for word in clean_text(text).split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def show_reports(counts):
    if not counts:
        print("No words were entered.")
        return
    print("Counts:", counts)
    number = int(input("How many top words? "))
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    print("Top words:", ordered[:number])
    print("Words appearing once:", [word for word in counts if counts[word] == 1])

    grouped = {}
    for word, amount in counts.items():
        if amount not in grouped:
            grouped[amount] = []
        grouped[amount].append(word)
    print("Words grouped by frequency:", grouped)

    by_length = {}
    for word in counts:
        length = len(word)
        if length not in by_length:
            by_length[length] = []
        by_length[length].append(word)
    print("Words grouped by length:", by_length)


def main():
    paragraph = input("Enter a paragraph: ")
    counts = count_words(paragraph)
    show_reports(counts)
    if counts:
        search = input("Word to search for: ").lower()
        print("Count:", counts.get(search, "not found"))


if __name__ == "__main__":
    main()
