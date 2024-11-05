from http.client import responses
from statistics import quantiles

import requests
from datetime import  datetime

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

today = datetime(year=2020, month=7, day=23)
print(today)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity":"15",
}

#
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

new_pixel_data = {
    "quantity": "4.5"
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

delete_endpoint = update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)