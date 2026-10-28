"""Examples based on the string data type class notes."""
data = "I love Python Programming"
print("Length:", len(data))
print("Count of P:", data.count("P"))
print("Starts with I:", data.startswith("I"))
print("Split:", data.split())
print("Uppercase:", data.upper())
print("Lowercase:", data.lower())

parts = ["I", "love", "Python", "Programming"]
print("Joined:", " ".join(parts))

# Remove vowels using a loop
text = "Python Programming"
result = ""
for char in text:
    if char not in "aeiouAEIOU":
        result += char
print("Without vowels:", result)

# Remove @ from an email-like string (demonstration only)
email = "invertis@gmail.com"
print("Without @:", email.replace("@", ""))
