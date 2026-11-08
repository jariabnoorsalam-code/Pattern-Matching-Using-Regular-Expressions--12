# Program to Perform Pattern Matching Using Regular Expressions
## Practical No: 12
### 1. Objective
To perform pattern matching using Regular Expressions in Python and extract numbers from a given text.
### 2. Programming Language
Python 3
### 3. Required Module
re (Regular Expression Module)
### 4. Source Code
```python
import re
text = "My phone number is 01712345678 and my age is 20."
pattern = r'\d+'
result = re.findall(pattern, text)
print("Original Text:", text)
print("Matched Patterns:", result)
```
### 5. Output
```text
Original Text: My phone number is 01712345678 and my age is 20.
Matched Patterns: ['01712345678', '20']
```
### 6. Working Procedure
1. Import the re module.
2. Create an input text.
3. Define a regular expression pattern.
4. Use re.findall() to find matching patterns.
5. Display the result.
### 7. Conclusion
I learned how to perform pattern matching using Regular Expressions in Python. I also learned how to extract numbers from a given text using the re module.
### Author Information
- Name: Jariab Noor Salam
- Roll: 356537
- Department: Computer Technology
- Semester: 3rd
- Institute: National Institute of Technology
