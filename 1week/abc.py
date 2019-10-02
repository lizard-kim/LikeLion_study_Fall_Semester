import json # python can import json!

# data type = dictionary
diary = { # It looks like javascript
    'id' : 3,
    'title' : 'I\'m starving...',
    'body' : 'Guk-bab is the best soul food in Korea!'
}

print(diary) # {'id': 3, 'title': "I'm starving...", 'body': 'Guk-bab is the best soul food in Korea!'}
print(type(diary)) # <class 'dict'>

diary_s = json.dumps(diary) # dumps : dict --> json

print(diary_s) # {'id': 3, 'title': "I'm starving...", 'body': 'Guk-bab is the best soul food in Korea!'}
print(type(diary_s)) # <class 'str'>

diary_back = json.loads(diary_s) # loads : json --> dict

print(diary_back)
print(type(diary_back)) # <class 'dict'>
