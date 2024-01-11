import string

def word_frequency(sentence):
    frequency = {}
    words = sentence.lower().translate(str.maketrans("", "", string.punctuation)).split()

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

# Test
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
