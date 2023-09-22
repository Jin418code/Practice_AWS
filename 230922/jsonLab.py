import json

list_ = ['Hello, world', 5, True, 89.5]
type(list_)

list

str_ = json.dumps(list_)
print(type(str_))

str
print(str_)


obj = json.loads(str_)
type(obj)

list
print(obj[2])

