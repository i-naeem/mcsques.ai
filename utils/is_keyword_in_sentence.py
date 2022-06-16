# sentencesWithKeywords = filter(
#     lambda sentence: len([k for k in keywords if k in sentence]) != 0, sentences)

def is_keyword_in_sentence(sentence: str, keywords: list[str]):
    """ Check if a sentence contains any keyword from keywords list

    Args:
        sentence (str): Sentence or text
        keywords (list[str]): List of keywords extracted from text

    Returns:
        boolean: True if sentence contain any keyword, false otherwise.
    """
    for keyword in keywords:
        if keyword in sentence:
            return True

    return False
