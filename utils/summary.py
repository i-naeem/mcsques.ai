from summarizer import Summarizer
from transformers import logging

# Shows some warning which I am not interest :)
logging.set_verbosity_error()


model = Summarizer('bert-large-uncased')


def summarize_text(text):
    """ Generates summary of give text using Bert Summarizer

    Args:
        text (string): A full text that would be summarize.

    Returns:
        string: Summary of `text`
    """

    summary = model(text, min_length=60, max_length=600, ratio=0.4)

    return summary
