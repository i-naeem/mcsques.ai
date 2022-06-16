#! ./Scripts/python.exe

from sentence_splitter import SentenceSplitter

splitter = SentenceSplitter(language="en")
text = "Hello World. How 0.4 is doing?"
sentences = splitter.split(text)

print(sentences)
