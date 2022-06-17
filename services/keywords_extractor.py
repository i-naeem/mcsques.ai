import pke
import string
from nltk.corpus import stopwords


def extract_keywords(text):
    """ Extract keywords from text using NLTK and PKE

    Args:
        text (str): Text from which keywords would be extracted.

    Returns:
        list[str]: List of keywords extracted from 
    """

    keywords = []
    pos = {'PROPN'}
    extractor = pke.unsupervised.MultipartiteRank()

    stoplist = list(string.punctuation)
    stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
    stoplist += stopwords.words('english')

    # Load Text
    extractor.load_document(input=text, stoplist=stoplist)
    # Select
    extractor.candidate_selection(pos=pos)
    # Extract
    extractor.candidate_weighting(alpha=1.1, threshold=0.75,  method='average')

    phrases = extractor.get_n_best(n=20)

    for key in phrases:
        keywords.append(key[0])

    return keywords
