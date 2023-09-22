import json

# with open("230922/sungjuk.json", "rt") as f:
#     result = json.load(f)
#     print(result[0] ['irum'])

src = "./sungjuk.json/"
with open('src', encoding='utf-8') as f:
    data = json.load(f)
    print(data)