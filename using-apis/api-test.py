'''
Author: Owen Barnett
Gets the movies from the specifed year, if a title is provided it prints all the movies
'''

import requests
import argparse

class movie_dataset:

    def __init__(self,year):
        '''
        Downloads all the movie data from the hydra movie api and puts it in a dictionary called data
        There are too many movies in the whole database so only movies from the specified year are taken
        '''

        url = "https://hydramovies.com/api-v2/?source=http://hydramovies.com/api-v2/current-Movie-Data.csv&movie_year={year}".format(year=year)
        raw_data = requests.get(url)
        self.data = raw_data.json()

    def print_titles(self):
        for moive_number in self.data:
            movie = self.data[moive_number]
            print(movie["Title"])

    def get_moive_by_name(self, movie_name):
        movie_name = movie_name.strip().lower()
        for movie_number in self.data:
            movie = self.data[movie_number]
            if movie["Title"].strip().lower().replace(" ","") == movie_name:
                return movie

        return -1


def main(args):
    movies = movie_dataset(args.year)
    if args.title is None:
        movies.print_titles()
    else:
        valid_movie = movies.get_moive_by_name(args.title)
        if valid_movie == -1:
            print("Movie not found")
        else:
            for attribute in valid_movie:
                print(str(attribute) + ": " + str(valid_movie[attribute]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gets the movies made in specifed year hydra movie api, '
                                                 'if a title is provided finds the movie and prints details')

    parser.add_argument('year',
                        metavar='year',
                        help='Which year the movies will be looked at',
                        type = int)

    parser.add_argument('--title',
                        metavar='title',
                        help='Search for a specific movie, remove spaces from movie title (Default: print all movie titles from the year)',
                        type = str)


    args = parser.parse_args()
    main(args)

