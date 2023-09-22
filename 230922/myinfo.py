import json

with open('D:/PythonHome/230922/myinfo.json', 'rt', encoding='utf-8') as f:
    data = json.load(f)
    print(type(data))