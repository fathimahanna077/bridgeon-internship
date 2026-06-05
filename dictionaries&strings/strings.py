# ==========================
# 1. Create a String
# ==========================

text = "  Hello Python World  "

print("Original String:")
print(text)

# ==========================
# 2. Indexing
# ==========================

print("\nIndexing:")
print(text[2])      # First letter H
print(text[-1])     # Last character

# ==========================
# 3. Slicing
# ==========================

print("\nSlicing:")
print(text[2:7])
print(text[:7])
print(text[8:])
print(text[::-1])   # Reverse string

# ==========================
# 4. f-Strings
# ==========================

name = "Hanna"
age = 21

print("\nf-String:")
print(f"My name is {name} and I am {age} years old.")

# ==========================
# 5. upper()
# ==========================

print("\nupper():")
print(text.upper())

# ==========================
# 6. lower()
# ==========================

print("\nlower():")
print(text.lower())

# ==========================
# 7. strip()
# ==========================

print("\nstrip():")
print(text.strip())

# ==========================
# 8. replace()
# ==========================

print("\nreplace():")
print(text.replace("Python", "Java"))

# ==========================
# 9. split()
# ==========================

print("\nsplit():")
words = text.strip().split()
print(words)

# ==========================
# 10. join()
# ==========================

print("\njoin():")
sentence = "-".join(words)
print(sentence)

# ==========================
# 11. find()
# ==========================

print("\nfind():")
print(text.find("Python"))
print(text.find("Java"))

# ==========================
# 12. count()
# ==========================

message = "apple banana apple mango apple"

print("\ncount():")
print(message.count("apple"))

# ==========================
# 13. startswith()
# ==========================

print("\nstartswith():")
print(text.strip().startswith("Hello"))
print(text.strip().startswith("Python"))

# ==========================
# 14. Membership Check
# ==========================

print("\nMembership Check:")
print("Python" in text)
print("Java" in text)

# ==========================
# 15. Length of String
# ==========================

print("\nLength:")
print(len(text))