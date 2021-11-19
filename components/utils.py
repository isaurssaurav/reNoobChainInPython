import hashlib
import json


def convert_to_sha256(text,isHex = False):
    sha = hashlib.sha256()
    sha.update(bytes(text, 'utf-8'))
    return sha.digest() if isHex == False else sha.hexdigest()

def get_difficulty_string(difficulty):
    difficulty_string = '0'
    for x in range(1,difficulty):
        difficulty_string += '0'
    return difficulty_string

def convert_obj_to_string(obj):
    return json.dumps(obj.__dict__)

def print_message(message):
    print('\n')
    print(message)