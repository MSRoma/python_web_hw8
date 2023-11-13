from config.models import Author , Quote
from mongoengine.errors import NotUniqueError
from config.db import connect
import json


author_data = 'authors.json'
quote_data = 'qoutes.json'

def data_load(data):
    with open(data, encoding='utf-8') as fd:
        data_json = json.load(fd)
    return(data_json)


def qoute(data_q):
    for el in data_load(data_q):
            author, *_ = Author.objects(fullname=el.get('author'))
            quote = Quote(quote=el.get('quote'), tags=el.get('tags'), author=author)
            quote.save()

def author(data_a):
    for el in data_load(data_a):
            try:
                author = Author(fullname=el.get('fullname'), born_date=el.get('born_date'),
                                born_location=el.get('born_location'), description=el.get('description'))
                author.save()
            except NotUniqueError:
                print(f"Автор вже існує {el.get('fullname')}")

if __name__ == "__main__":
    author(author_data)
    qoute(quote_data)

# author = Author(fullname=el.get('fullname'), born_date=el.get('born_date'),
#                                 born_location=el.get('born_location'), description=el.get('description'))
# # потім - створення об'єктів Record
# record1 = Record(description='Buying sausage')
# record2 = Record(description='Buying milk')
# record3 = Record(description='Buying oil')
# #  Останнє - створюємо об'єкт Note і зберігаємо його
# Notes(name='Shopping', records=[record1, record2, record3], tags=[tag, ]).save()

# Notes(name='Going to the movies', records=[Record(description='Went to see the Avengers'), ], tags=[Tag(name='Fun'), ]).save()