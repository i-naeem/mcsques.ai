#! ./Scripts/python.exe

# from utils.keywords_extractor import extract_keywords
# from utils.text_summarizer import summarize_text
# from sentence_splitter import SentenceSplitter
from cli import parser

args = parser.parse_args()

# Step 0: Setup CLI
# Step 1: Extract Keywords
# Step 2: Summarize Text
# Step 3: Filter Extracted Keywords from Summarize Text
# Step 4: Filter Sentence Where Keywords Appear
# Step 5: Replace Keyword with ____ in Sentence
# Step 6: Find at least 3 Common Words with Keyword
# Step 7: Create an Multiple Choice Question
