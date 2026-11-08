import re
# Input text
text = "My phone number is 01712345678 and my age is 20."
# Regular expression pattern
pattern = r'\d+'
# Perform pattern matching
result = re.findall(pattern, text)
# Display output
print("Original Text:", text)
print("Matched Patterns:", result)
