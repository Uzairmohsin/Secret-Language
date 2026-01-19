# Secret Code Language using Python

This repository contains a Python program that translates normal English text into a secret coded language and can also decode it back to the original message.  
The project focuses on string manipulation, conditional logic, and basic encoding–decoding concepts in Python.

---

## Problem Description

The task is to design a simple secret language with defined rules for encoding and decoding words based on their length.  
This activity helps in understanding how strings can be transformed programmatically using logical conditions.

---

## Encoding Rules

- If a word contains **at least 3 characters**:
  - Remove the first letter of the word
  - Append it to the end of the word
  - Add **three random characters** at the beginning and at the end
- If a word contains **less than 3 characters**:
  - Simply reverse the word

---

## Decoding Rules

- If a word contains **less than 3 characters**:
  - Reverse the word to get the original message
- If a word contains **3 or more characters**:
  - Remove the three random characters from the start and end
  - Move the last letter back to the beginning to recover the original word

---

## Key Concepts Used

- String slicing and manipulation
- Conditional statements (`if-else`)
- Random character generation
- Encoding and decoding logic
- User input handling