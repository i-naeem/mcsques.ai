#! ./Scripts/python.exe

import pke
import string
from transformers import logging
from summarizer import Summarizer
from nltk.corpus import stopwords

logging.set_verbosity_error();

full_text = '''
Everyone knows that every successful blogger make money. Yes, it is fact, if you planning this then make sure that you niche is profitable. Making money with blog have different ways, you can earn commission using affiliate link on your blog, you can also make money with google AdSense, etc.

Google AdSense works based on CPC (Click Per Rate) by matching ads to your site based on your content and visitors. The ads are created and paid for by advertisers who want to promote their products. Since these advertisers pay different prices for different ads.

There is also google free tools where you can find high CPC (click per rate) keyword that use in your blog.

To do keyword research, find high CPC keyword, click on Google Keyword Planner

Here is it, go to Google Keyword Planner and type your keyword, I find “Insurance” in United States, You can search keyword by location too. At the end you can see “Avg Monthly Searches” means insurance have almost 100k – 1M monthly search, After that you can see “competition” according to google keyword planner competition on insurance keyword is medium, and last one is “Top of Pages bid” this is actual price advertisers pay to google to ranking their ads on this keyword.

You’ll earn commission 60% of this price when someone come to your site by search insurance keyword on google.
'''


def get_nouns_multipartite(text):
    out=[]
    extractor = pke.unsupervised.MultipartiteRank()

    stoplist = list(string.punctuation)
    stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-']
    stoplist += stopwords.words('english')
    
    extractor.load_document(input=text,stoplist=stoplist)
    #    not contain punctuation marks or stopwords as candidates.
    pos = {'PROPN'}
    #pos = {'VERB', 'ADJ', 'NOUN'}
    
    extractor.candidate_selection(pos=pos, )
    # 4. build the Multipartite graph and rank candidates using random walk,
    #    alpha controls the weight adjustment mechanism, see TopicRank for
    #    threshold/method parameters.
    extractor.candidate_weighting(alpha=1.1,
                                  threshold=0.75,
                                  method='average')
    keyphrases = extractor.get_n_best(n=20)
    for key in keyphrases:
          out.append(key[0])

    return out



keywords = get_nouns_multipartite(full_text) 
model = Summarizer('bert-large-uncased')
result = model(full_text, min_length=60, max_length = 500 , ratio = 0.4)
summarized_text = ''.join(result)

filtered_keys=[]
for keyword in keywords:
    if keyword.lower() in summarized_text.lower():
        filtered_keys.append(keyword)

print(filtered_keys)