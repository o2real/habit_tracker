from http.client import responses

import requests

USERNAME = "jioh"
TOKEN = "asdjflksjqwer123djfl"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",


}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs "

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}


response = requests.post(url=graph_endpoint, json=graph_config)
print(response.text)

