def word_count(text):
    #Returns count of words in a file
    #number_of_words = text.split()
    return len(text.split())

def count_characters(text):
    #Returns a dictionary with counts of each character in lowercase
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_characters(char_dict):
    #Returns a dictionary of alphabetic characters sorted by count descending
    char_list = [
        {"char": char, "num": count}
        for char, count in char_dict.items()
        if char.isalpha()
    ]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list