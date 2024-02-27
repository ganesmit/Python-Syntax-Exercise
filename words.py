def print_upper_words(words):
    """Print out each word on seperate line in all uppercase.
        print_upper_words(["jack", "and", "jill", "went, "up", "the", "hill"])
        Jack
        And 
        Jill
        Went
        Up
        The
        Hill
    """
    
    for word in words:
        print(word.upper())

print_upper_words(["jack", "and", "jill", "went", "up", "the", "hill"])

def print_upper_words_e(words):
    """Print out each word starting with "E" or "e" on a seperate line in all uppercase.
        print_upper_words_e(["Evan", "John", "evelyn", "harry"])
        Evan
        Evelyn
    """
    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print(word.upper())

print_upper_words_e(["Evan", "John", "evelyn", "harry"])

def print_upper_words_by_letter(words, by_letter):
    """Print out each word starting with "Y" or "B" on a seperate line in all uppercase.
        print_upper_words_by_letter(["Barbara", "Yasmine", "betty", "yori"])
        Barbara
        Yasmine 
    """
    for word in words:
        for letter in by_letter:
            if word.startswith(letter):
                print(word.upper())

print_upper_words_by_letter(["Barbara", "Yasmine", "betty", "yori"], by_letter=["B", "Y"])