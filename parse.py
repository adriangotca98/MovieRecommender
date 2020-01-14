import play_csv
import string
from nltk.tokenize import word_tokenize
from gensim.models.word2vec import Word2Vec
user_input = ['toy']
words = ['The', 'flowers', 'are', 'beautiful']
movies = play_csv.play_csv()


def get_data_set():
    data_set = []
    for movie in movies:
        title = movie.get('Title')
        genres = movie.get('Genre')
        tags = movie.get('Tags')

        exclude = set(string.punctuation + string.digits)

        title = ''.join(ch for ch in title if ch not in exclude)
        for i in word_tokenize(title):
            data_set.append(i.lower())

        for genre in genres:
            for j in word_tokenize(genre):
                data_set.append(j.lower())

        for tag in tags:
            if tag is not None:
                for k in word_tokenize(tag):
                    data_set.append(k.lower())
    return data_set


print(get_data_set())


def parse(input):
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in input if ch not in exclude)
    temp = []
    for i in word_tokenize(text):
        temp.append(i.lower())
    return temp


def get_similarities(text):
    words = parse(text)
    data_set = get_data_set()
    print('Start')
    cbow_model = Word2Vec(data_set, min_count=1, size=1000, window=100)
    similarities = []
    for word in words:
        cbow_prediction = cbow_model.wv.most_similar(word, topn=1)
        syn = cbow_prediction[0][0]
        similarities.append(syn)
        print(syn)


get_similarities(user_input)
