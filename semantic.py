# semantic.py

import spacy

# Load the simpler spaCy model 'en_core_web_sm'
# This model is smaller and simpler than 'en_core_web_md'
# It has a smaller vocabulary and fewer vectors
nlp_sm = spacy.load('en_core_web_sm')

# Input words
tokens = nlp_sm('cat monkey banana')

# Print similarities
for token1 in tokens:
    for token2 in tokens:
        print(f"{token1.text} - {token2.text}: {token1.similarity(token2)}")

# Observations:
# - The model 'en_core_web_sm' is a smaller and simpler version than 'en_core_web_md'.
# - The similarity scores may be different compared to 'en_core_web_md' due to the reduced size and complexity.
# - Despite being smaller, the model still captures some semantic relationships, such as animals being similar.

# Additional notes:
# - The similarity score ranges between 0 and 1, where 1 indicates the highest similarity.
# - The output is symmetrical, i.e., the similarity of A to B is the same as B to A.
