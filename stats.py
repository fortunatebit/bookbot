def sort_on(dict):
    return dict["value"]

def get_num_words(book):
    return len(book.split())

def get_num_characters(book):
    character_frequency = {}
    for character in book.lower():
        if not character in character_frequency:
            character_frequency[character] = 1
        else:
            character_frequency[character] += 1
    return character_frequency

def sort_characters(character_dict):
    list_of_dictionaries = []
    for character in character_dict:
        small_dict = {"character": None, "value": None}
        if character.isalpha():
            small_dict["character"] = character
            small_dict["value"] = character_dict[character]
            list_of_dictionaries.append(small_dict)
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries