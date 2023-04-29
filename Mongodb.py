import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['MyDictionary']
collection = db['words']


def get_definition(word):
    result = collection.find_one({'word': word})
    if result:
        return result['definition']
    else:
        return None


def add_word(word, definition):
    result = collection.insert_one({'word': word, 'definition': definition})
    return result.inserted_id


def remove_word(word):
    result = collection.delete_one({'word': word})
    return result.deleted_count


while True:
    action = input(''' Menu 
"a" add word.
"b" remove word.  
"c" view definition.
"s" exit.
\n enter an option: ''')

    if action == 's':
        break
    elif action == 'a':
        word = input('enter word: ')
        definition = input('enter definition: ')
        add_word(word, definition)
    elif action == 'b':
        word = input('remove word: ')
        remove_word(word)
    elif action == 'c':
        word = input('view definition: ')
        definition = get_definition(word)
        if definition:
            print(definition)
        else:
            print('word not found')
