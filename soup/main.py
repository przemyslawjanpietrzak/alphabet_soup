def group_input(word):
    chars = list(word)
    return {char: chars.count(char) for char in set(chars)}


def is_empty(grouped_chars):
    for char_count in grouped_chars.values():
        if char_count != 0:
            return False
    return True


def can_make_word(word, letters):
    """
    check if is enough letters in soup to make word
    :params word: word to make from soup's letters
    :type string
    :params letters: list/array or generator of available letters in soup
    :type Array<String>
    :returns Boolean
    """
    grouped_chars = group_input(word)
    for char in letters:

        if is_empty(grouped_chars):
            return True

        if char in grouped_chars and grouped_chars[char] > 0:
            grouped_chars[char] -= 1

    return is_empty(grouped_chars)
