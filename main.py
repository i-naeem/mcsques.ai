#! ./Scripts/python.exe

from cli import args
from sentence_splitter import SentenceSplitter
from services.keywords_extractor import extract_keywords

# Step 0: Setup CLI [*]
rfile = args.input
ofile = args.output

# Step 1: Read Text from File [*]
text = rfile.read()

# Step 2: Extract Keywords [*]
print('Extracting Keywords')
keywords = extract_keywords(text)

# Step 3: Split Text into Sentences [*]
splitter = SentenceSplitter(language="en")
print('Splitting Text to Sentences')
sentences = splitter.split(text)


# Step 4: Filter Sentences by Sentences which have any Extracted Keyword [*]
print('Filtering Sentences')
filtered_sentences = []

for sentence in sentences:
    for keyword in keywords:
        if keyword.lower() in sentence.lower():
            filtered_sentences.append({
                "question": sentence,
                "correct_option":  keyword,
            })
            break


for mcqs in filtered_sentences:
    print(mcqs['question'], ' => ', mcqs['correct_option'])

# Step 5: Replace Keyword with ____ in Sentence
# Step 6: Find at least 3 Common Words with Keyword
# Step 7: Create an Multiple Choice Question
