import json

data = {
    "nama": "John",
    "umur": 30,
    "mahasiswa": True,
    "hobi": ["membaca", "bermain gitar"]
}

string_json = json.dumps(data)
print(string_json)
