import pymongo
from pymongo import MongoClient

client = MongoClient()

client = MongoClient('mongodb://localhost:27017')

db = client['Anthony']
collection = db['task']


def get_definicion(palabra):
    result = collection.find_one({'palabra': palabra})
    if result:
        return result['definicion']
    else:
        return None


def get_salir(palabra):
    result = collection.find_one({'palabra': palabra})
    if result:
        return result['definicion']
    else:
        return None


def add_palabra(palabra, definicion):
    result = collection.insert_one({'palabra': palabra, 'definicion': definicion})
    return result.inserted_id


def remove_palabra(palabra):
    result = collection.delete_one({'palabra': palabra})
    return result.deleted_count


while True:
    action = input(''' Menu 
"a" insertar palabra.
"b" remover palabra.  
"c" ver definicion.
"s" salir.
\n ingresa una opcion: ''')

    if action == 's':
        break
    elif action == 'a':
        palabra = input('ingresar palabra: ')
        definicion = input('ingresar definicion: ')
        add_palabra(palabra, definicion)
    elif action == 'b':
        palabra = input('remover palabra: ')
        remove_palabra(palabra)
    elif action == 'c':
        palabra = input('ver definicion: ')
        definicion = get_definicion(palabra)
        if definicion:
            print(definicion)
        else:
            print('palabra no encontrada')

