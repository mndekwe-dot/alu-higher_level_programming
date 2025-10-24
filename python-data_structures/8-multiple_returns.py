def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.
    
    Args:
        sentence: The input string
    
    Returns:
        A tuple containing (length, first_character)
        If the string is empty, first_character is None
    """
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return (length, first_char)
