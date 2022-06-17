#! ./Scripts/python.exe

from cli import args
from sentence_splitter import SentenceSplitter
from services.text_summarizer import summarize_text
from services.keywords_extractor import extract_keywords

# Step 0: Setup CLI [*]
rfile = args.input
ofile = args.output

# Step 1: Read Text from File [*]
text = rfile.read()

# Step 2: Extract Keywords [*]
print('Extracting Keywords')
keywords = extract_keywords(text)

# Step 3: Summarize Text [*]
print('Summarizing Text')
summary = summarize_text(text)

# Step 4: Filter Extracted Keywords from Summarize Text [*]
print('Filtering Keywords')
filtered_keywords = list(filter(lambda k: k in summary, keywords))


# Step 5: Split Text into Sentences [*]
splitter = SentenceSplitter(language="en")
print('Splitting Text to Sentences')
sentences = splitter.split(text)


# Step 6: Filter Sentences by Sentences which have any Extracted Keyword [*]
print('Filtering Sentences')
filtered_sentences = []

for sentence in sentences:
    for keyword in keywords:
        if keyword in sentence:
            filtered_sentences.append({
                "question": sentence,
                "correct_option":  keyword,
            })
            break


for mcqs in filtered_sentences:
    print(mcqs['question'], ' => ', mcqs['correct_option'])

# Step 7: Replace Keyword with ____ in Sentence
# Step 8: Find at least 3 Common Words with Keyword
# Step 9: Create an Multiple Choice Question
