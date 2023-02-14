import spacy
nlp = spacy.load('en_core_web_sm')

#== what is interesting ==#

# It is interesting that it finds similarities between simple 
# concepts, such as fruit/animal/diet. I would like to test
# the model to see how far it can go

#== own example ==#

tokens = nlp('housecat wolf eagle tuna')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# They are all animals
# 1 and 2 are both mammals
# 2, 3, 4 are wild animals
# 1 and 3 eats 4
# 2 and 3 are apex predators
# 1, 2, 3 live on land

# The similarity values are surprisingly low.

#== md vs sm ==#

# sm UserWarning - 'no word vectors loaded, so the result of the Token.similarity 
# method will be bas on the tagger, parser and NER'

# With sm, all of the values are 2-3x higher