import requests
import pandas


def get_books_by_name(name):
    books = requests.get('http://openlibrary.org/search.json?title={}'.format(name))
    titles = []
    authorsNames = []
    keys = []
    for book in books.json()['docs']:
        titles.append(book['title'])
        if 'author_name' in book:
            authorsNames.append(book['author_name'])
        else:
            authorsNames.append('Unknown')
        keys.append(book['key'].split('/')[-1])

    books = pandas.DataFrame({'title': titles,
                              'author': authorsNames,
                              'key': keys},
                             columns=['title', 'author', 'key'])
    return books


def get_book_by_key(book_key):
    book = requests.get('http://openlibrary.org/works/{}.json'.format(book_key))
    return book.json()