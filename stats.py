def count_words(file_contents):
    words = file_contents.split()
    word_count=len(words)
    return word_count

def count_characters(file_contents):
    text = file_contents.lower()
    chars = {}
    for letter in text:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    return chars

def sort_on(list_chars):
    return list_chars["num"]

def sort_dict(chars):
    list_chars = []
    for i in chars:
        dict = {}
        dict["char"] = i
        dict["num"] = chars[i]
        list_chars.append(dict)
    
    list_chars.sort(reverse=True,key=sort_on)
    return list_chars