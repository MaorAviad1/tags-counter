import re
from collections import Counter

def create_table(text):
    # Split the text into a list of words
    words = re.findall(r'\b\w+\b', text)
    # Create a list of two-word phrases
    phrases = [words[i] + ' ' + words[i+1] for i in range(len(words)-1)]

    # Use the Counter class to count the occurrences of each word and phrase
    word_counts = Counter(words)
    phrase_counts = Counter(phrases)

    # Print the results in a tabular format
    print('Word/Phrase\tCount')
    for word, count in word_counts.items():
        print(word + '\t' + str(count))
    for phrase, count in phrase_counts.items():
        print(phrase + '\t' + str(count))

def create_table_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    create_table(text)

file_path = 'C:/Users/Dana/PycharmProjects/tags-counter/New Text Document.txt'
create_table_from_file(file_path)
