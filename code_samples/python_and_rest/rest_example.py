#!/usr/bin/env python

from pprint import pprint

import requests

BASE_URL = "https://swapi.dev/api"


def get_request(request: str) -> dict:
    """
    Performs an HTTP GET request.

    Args:
      request: A string containing the unique URI for the GET request
    Returns:
      A dict containing the results of the HTTP GET request.
    """
    url = f"{BASE_URL}/{request}"
    resp = requests.get(url)
    return resp.json()


def look_up_person(person_id: int) -> dict:
    """
    Looks up a person given the ID.

    Args:
      person_id: An integer specifying the ID of the person to look up.
    Returns:
      A dict containing details of the requested person.
    """
    request = f"people/{person_id}"
    person = get_request(request)
    return person


def main():
    person = look_up_person(1)
    pprint(person)


if __name__ == "__main__":
    main()
