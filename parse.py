import play_csv
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from gensim.models.word2vec import Word2Vec

text = ['action movie will ferrell']
movies = play_csv.play_csv()


def get_data_set():
    data_set = []
    for movie in movies:
        title = movie.get('Title')
        genres = movie.get('Genre')
        tags = movie.get('Tags')

        exclude = set(string.punctuation + string.digits)
        title = ''.join(ch for ch in title if ch not in exclude)

        for i in sent_tokenize(title):
            temp = []
            for j in word_tokenize(i):
                temp.append(j.lower())
            data_set.append(temp)

        for genre in genres:
            for i in sent_tokenize(genre):
                temp = []
                for j in word_tokenize(i):
                    temp.append(j.lower())
                data_set.append(temp)

        for tag in tags:
            if tag is not None:
                for i in sent_tokenize(tag):
                    temp = []
                    for j in word_tokenize(i):
                        temp.append(j.lower())
                    data_set.append(temp)
    return data_set


def parse(user_input):
    exclude = set(string.punctuation)
    user_input = ''.join(ch for ch in user_input if ch not in exclude)
    temp = []
    for i in word_tokenize(user_input):
        temp.append(i.lower())
    return temp


def get_similarities(user_input):
    words = parse(user_input)
    data_set = get_data_set()
    print('Start')
    cbow_model = Word2Vec(data_set, min_count=1, size=100, window=10)
    similarities = []
    for word in words:
        cbow_prediction = cbow_model.wv.most_similar(word, topn=1)
        syn = cbow_prediction[0][0]
        similarities.append(syn)
    return similarities


def get_recommendations(user_input):
    movies_recommendations = []
    similarities = get_similarities(user_input)
    for word in similarities:
        for movie in movies:
            title = movie.get('Title')
            genres = movie.get('Genre')
            tags = movie.get('Tags')
            if word in title or word in genres or word in tags:
                movies_recommendations.append(movie)
    sorted_movies = sorted(movies_recommendations, key=lambda j: j['Rating'], reverse=True)
    top_movies = []
    for i in range(10):
        top_movies.append(sorted_movies[i])
    print(top_movies)


get_recommendations(text)
