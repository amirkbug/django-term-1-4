import requests



url = "http://127.0.0.1:8000/services/api/v1/services"

data = {
    "title": "newhasangholi",
    "content": "x1",
    "description": "x3",
    "catalog_file": "x",
    "catalog_doc": "x",
    "status": True,
    "creator": 1,
    "specials": [
        1
    ],
    "category": [
        1
    ]
}



response = requests.post(url, data=data)
if response.status_code == 201:
    print("success")