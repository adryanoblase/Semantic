# semantic.py

import spacy

# Load the simpler spaCy model 'en_core_web_sm'
nlp = spacy.load('en_core_web_sm')

# Input words
tokens = nlp('cat apple monkey banana ')

# Comment on similarities
# - Cat and monkey seem to be similar because they are both animals.
# - Banana and apple are similar because they are both fruits.
# - Interestingly, monkey and banana have a higher similarity than monkey and apple.
#   This suggests that the model captures the relationship that monkeys eat bananas.

# Another interesting observation:
# - Cat does not have any significant similarity with any of the fruits, while monkey does.
#   This implies that the model may not explicitly recognize transitive relationships in its calculation.

# Example to demonstrate the model's ability to recognize relationships:
# Let's create a new example with a concept of "vehicle" and "speed."
# Here, "car" and "bike" are both related to the concept of a vehicle, and "speed" is related to both "car" and "bike."
# As a result, we might expect "car" and "bike" to have some similarity due to their common association with "speed."

new_example = nlp('car bike speed')
for token1 in new_example:
    for token2 in new_example:
        print(token1.text, token2.text, token1.similarity(token2))
