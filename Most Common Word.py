from collections import Counter

def most_common_word(text):
    # Converting all letters to lowercase to ensure case insensitivity
    words = text.lower().split()
    # Counting the frequency of each word
    word_counts = Counter(words)
    # Extracting the most common word
    most_common = word_counts.most_common(1)
    return most_common[0][0] if most_common else None

# Example usage
text = "This is a sample text that contains some sample words."
result = most_common_word(text)
print(f"The most common word is: {result}")
