#Author: Owen Barnett

import sys
import csv
import os

def get_books(file):
    '''
     takes a file and return a list of the book names
     assumes that file is a valid path to a csv file
    '''
    books = set()
    reader = csv.reader(open(file, newline=''))
    for row in reader:
        books.add(row[0])

    return list(books)

def get_authors(file):
    '''
    takes a file and return a list of the author names
    assumes that file is a valid path to a csv file
    '''
    cut = "1234567890()-"
    authors = set()
    reader = csv.reader(open(file, newline=''))
    for row in reader:
        temp = "".join(i for i in row[2] if not i in cut).strip()
        loc = temp.find(" and ")
        if loc != -1:
            authors.add(temp[0:loc].strip())
            authors.add(temp[loc+4:].strip())
        else:
            authors.add(temp)
    return list(authors)


def sort_authors(authors, dir):
    '''
    returns a sorted list of authors
    assumes that authors is a list of names
    direction is either True or False, True sorts in lexicon order false sorts in reverse lexicon order
    '''
    authors.sort(key = lambda x: x.split(" ")[-1]+x.split(" ")[0], reverse = dir)
    return authors

def sort_books(books, dir):
    '''
    returns a sorted list of book names
    assumes that books is a lsit of book names
    direction is either True or False, True sorts in lexicon order false sorts in reverse lexicon order
    '''
    books.sort(reverse = dir)
    return books

def valid_input():
    '''
    checks if the command line inputs follow the pattern: input-file action [sort-directoin]
    returns true if the inputs are good
    returns false if the inputs are bad
    '''
    if len(sys.argv) > 1 and ".csv" in sys.argv[1] and os.path.exists(sys.argv[1]):
        if len(sys.argv)>2:
            if sys.argv[2] == "authors" or sys.argv[2] == "books":
                if len(sys.argv) == 3:
                    return True
                if (len(sys.argv) == 4) and (sys.argv[3] == "reverse" or sys.argv[3]=="forward"):
                    return True

    return False

def main():
    if not valid_input():
        print('Usage: input-file action [sort-direction]', file=sys.stderr)
        quit()
    direction = sys.argv[len(sys.argv)-1] == "reverse"
    list = []
    if sys.argv[2] == "authors":
        list = get_authors(sys.argv[1])
        list = sort_authors(list,direction)
    else:
        list = get_books(sys.argv[1])
        list = sort_books(list, direction)
    for k in list:
        print(k)

if __name__== "__main__":
  main()