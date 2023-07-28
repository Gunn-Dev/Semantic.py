import spacy

def calculate_similarity(text):
    nlp = spacy.load('en_core_web_lg')
    tokens = nlp(text)
    for token1 in tokens:
        for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))

if __name__ == "__main__":
    example_text = "The cat ate a banana while watching the monkey."
    calculate_similarity(example_text)
