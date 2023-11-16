#rom bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from config.db import mongoclient

mongoclient()

# db = mongoclient.
# result = db.authors.find({})
# for el in result:
#     print(el)

# notes = Notes.objects()
# for note in notes:
#     print("-------------------")
#     records = [f'description: {record.description}, done: {record.done}' for record in note.records]
#     tags = [tag.name for tag in note.tags]
#     print(f"id: {note.id} name: {note.name} date: {note.created} records: {records} tags: {tags}")

# @cache
# def find_by_tag(tag: str) -> list[str | None]:
#     print(f"Find by {tag}")
#     quotes = Quote.objects(tags__iregex=tag)
#     result = [q.quote for q in quotes]
#     return result