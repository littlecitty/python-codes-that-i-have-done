#38. Count frequency of words in sentence.
sentence = input("enter a sentence: ").strip().split()
word_count = {}

for word in sentence:
    word_count[word] = word_count.get(word, 0) + 1  # increment count

# Make output attractive using join
print(", ".join(f"{word}: {count}" for word, count in word_count.items()))

# Pythonic version
from collections import Counter
counts = Counter(input("enter a sentence: ").split())
print(", ".join(f"{word}: {count}" for word, count in counts.items()))



#pythonicw way
from collections import Counter

sentence = input("enter a sentence: ").split()
print(", ".join(f"{word}: {count}" for word, count in Counter(sentence).items()))

