#!/usr/bin/env python
from webexteamssdk import WebexTeamsAPI

from config import Teams

webexteams = WebexTeamsAPI(access_token=Teams.ACCESS_TOKEN)


def info_about_me():
    me = webexteams.people.me()
    return me


def list_roles():
    roles = webexteams.roles.list()
    for role in roles:
        print(role)


def list_rooms():
    rooms = webexteams.rooms.list()
    for room in rooms:
        print(room)


def list_users():
    users = webexteams.people.list()
    for user in users:
        print(user)
