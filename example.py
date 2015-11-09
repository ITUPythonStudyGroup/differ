from delta import *
import json

person = {
    'name': 'Andreas',
    'skills': {
        'matlab': 3,
        'swift': 2
    },
    'age': 25
}

personLater = {
    'name': 'Andreas',
    'skills': {
        'python': 3,
        'swift': 3
    },
    'age': 26
}

print("Delta format:")
print(json.dumps(delta(person, personLater), indent = 4))
print("result of delta plus merge:")
print(json.dumps(merge(person, delta(person, personLater)), indent = 4))
