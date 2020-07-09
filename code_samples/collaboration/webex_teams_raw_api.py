#!/usr/bin/env python
import requests

from config import Teams

BASE_URL = "https://webexapis.com/v1/"
HEADERS = {
    "Authorization": f"Bearer {Teams.ACCESS_TOKEN}",
    "Content-Type": "application/json",
}


def api_post(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    return requests.post(url, headers=HEADERS).json()


def api_get(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    return requests.get(url, headers=HEADERS).json()


def list_rooms():
    rooms = api_get("rooms")
    for room in rooms["items"]:
        print(room)
    return rooms


def list_users():
    users = api_get("people")
    for user in users["items"]:
        print(user)
    return users
