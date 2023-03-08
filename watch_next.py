import spacy
nlp = spacy.load('en_core_web_md')

with open('movies.txt', 'r') as m:
    movies = m.readlines()

planet_hulk = ['Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator']

# Build list of similarity values
sims = []
# Compare planet hulk string to each film in movies.txt, add similarity to list
for summary in planet_hulk:
    summary = nlp(summary)
    for film in movies:
        film = nlp(film)
        sims.append(film.similarity(summary))

# Find max value, index
max_value = max(sims)
index = sims.index(max_value)

# Split by the colon to separate the movie name and print
similar_movie = movies[index].split(':')
print(f'The movie most similar to \'Planet Hulk\' is: {similar_movie[0]}')