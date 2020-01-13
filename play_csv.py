import csv

movies_csv_file = open("ml-25m\\movies.csv", "r", encoding="UTF8")
links_csv_file = open("ml-25m\\links.csv", "r", encoding="UTF8")
tags_csv_file = open("ml-25m\\tags.csv", "r", encoding="UTF8")
ratings_csv_file = open("ml-25m\\ratings.csv", encoding="UTF8")
movies_csv = csv.reader(movies_csv_file)
links_csv = csv.reader(links_csv_file)
tags_csv = csv.reader(tags_csv_file)
ratings_csv = csv.reader(ratings_csv_file)
movies = []
for i in range(300000):
    movies.append({})
for row_movies, row_links in zip(movies_csv, links_csv):
    movie = {'Title': row_movies[1], 'Genre': row_movies[2].split("|"), 'imdbId': row_links[1],
             'tmdbId': row_links[2], 'RatingsSum': 0, 'NrRatings': 0, 'Rating': 0, 'Tags': []}
    if row_movies[0].isdigit():
        movies[int(row_movies[0])] = movie
nr = 0
for row_ratings in ratings_csv:
    nr += 1
    if row_ratings[1].isdigit():
        ind = int(row_ratings[1])
        movies[ind]['RatingsSum'] += float(row_ratings[2])
        movies[ind]['NrRatings'] += 1
    if nr % 10000000 == 0:
        print(nr)
for movie in movies:
    if len(movie) > 0:
        if movie['NrRatings']!=0:
            movie['Rating'] = movie['RatingsSum'] / movie['NrRatings']
        movie.pop('RatingsSum')
        movie.pop('NrRatings')
for tag in tags_csv:
    if tag[0].isdigit():
        movies[int(tag[1])]['Tags'].append(tag[2])
for movie in movies:
    if movie.get('Tags')==[]:
        movie.pop('Tags')
    print(movie)
