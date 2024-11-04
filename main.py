from http.client import responses

import requests

USERNAME = "jioh"
TOKEN = "asdjflksjqwer123djfl"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",


}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs "

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,

}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": "20241104",
    "quantity":"9.74",
}


requests.post(url=pixel_creation_endpoint), json=pixel_data, headers=headers