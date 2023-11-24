# Semantic Similarity Analyser

## Description

This Python script demonstrates semantic similarity using the spaCy library. The script loads the smaller spaCy English model 'en_core_web_sm' and calculates the semantic similarity between a set of input words. It provides insights into how the model perceives the relationships between these words.

## Table of Contents
- [Usage](#usage)
- [Observations](#observations)
- [Additional Notes](#additional-notes)
- [Credits](#credits)
- [Contact](#contact)
- [License](#license)

# How to Use
Install spaCy:
Make sure you have spaCy installed. If not, you can install it using:
pip install spacy

# Download spaCy Model:
Download the spaCy English model 'en_core_web_sm' by running:
python -m spacy download en_core_web_sm

# Run the Script:
Execute the script to analyse semantic similarity. The script uses the 'en_core_web_sm' model to evaluate the relationships between input words.
python semantic.py

# Observations
The 'en_core_web_sm' model is a smaller and simpler version of the spaCy model.
The similarity scores may differ from larger models due to reduced vocabulary and complexity.
Despite its smaller size, the model captures some semantic relationships, offering insights into word similarities.

# Additional Notes
The similarity score ranges between 0 and 1, where 1 indicates the highest similarity.
The output is symmetrical, i.e., the similarity of A to B is the same as B to A.

# Credits
This project was created by:

[Adriano Mama]
GitHub: [adryanoblase]

# Contact
If you have any questions or feedback regarding this project, feel free to contact the author:

Name: [Adriano]
Email: [adrianoblase99@gmail.com]

# License
© 2023 [Adriano Mama]. All rights reserved.
