from pdfminer.high_level import extract_text
# to run (only works through shell): python pdfExtractor.py

text = extract_text("samples/StudyZots_example1.pdf")
print(text)
