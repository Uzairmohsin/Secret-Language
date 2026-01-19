import random

letters = "abcdefghijklmnopqrstuvwxyz"

word = input("Enter a word: ")

if len(word) < 3:
    encoded = word[::-1]
else:

    r1 = random.choice(letters)
    r2 = random.choice(letters)
    r3 = random.choice(letters)

    r4 = random.choice(letters)
    r5 = random.choice(letters)
    r6 = random.choice(letters)

  
    new_word = word[1:] + word[0]

   
    encoded = r1 + r2 + r3 + new_word + r4 + r5 + r6

print("Encoded:", encoded)


if len(encoded) < 3:
    decoded = encoded[::-1]
else:
   
    core = encoded[3:-3]

   
    decoded = core[-1] + core[:-1]

print("Decoded:", decoded)
