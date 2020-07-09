#!/usr/bin/env python
"""
Example module to demonstrate the use of a class in querying an API. The module would
be imported via an absolute or relative import and instantiated to an object as
demonstrated in main().
"""

import requests


class SWAPI(object):
    """
    A relatively simple class used to query the Star Wars API.
    """

    def __init__(self, verify: bool = True):
        """
        Constructs the object upon instantiation. This sets the attributes of the
            object. If the API required authentication, the arguments would include
            things like username and password or auth token. This allows encapsulation
            between multiple instantiations of the object.

        Attrs:
          base_url: A string containing the portion of the URL that will be common to
              all requests
          verify:
          sess:
        """
        self.base_url = "https://swapi.dev/api"
        self.verify = verify
        self.sess = requests.Session()

    def _get(self, request: str) -> dict:
        """
        Performs an HTTP GET request given the unique URI of the request.

        Args:
          request: A string containing the unique URI of the query
        Returns:
          A dict containing the reqults of the query
        """
        url = f"{self.base_url}/{request}"
        resp = self.sess.get(url, verify=self.verify)
        return resp.json()

    def _get_full_url(self, url: str) -> dict:
        """
        Performs an HTTP GET request given the full URL of the request. Used for
            iterating over URLs returned in other requests.

        Args:
          url: A string containing the URL to query
        Returns:
          A dict containing the results of the query
        """
        resp = self.sess.get(url, verify=self.verify)
        return resp.json()

    def find_person(self, person_id: int) -> dict:
        """
        Finds details for a person given the person's ID.

        Args:
          person_id: An int specifying the ID of the person to look up
        Returns:
          A dict containing the details for the requested person.
        """
        try:
            request = f"people/{int(person_id)}"
        except ValueError:
            raise ValueError("Hey dummy you need the person ID, not the name!")
        return self._get(request)

    def find_film(self, film_id: int) -> dict:
        """
        Finds details for a film given the film's ID.

        Args:
          film_id: An int specifying the ID of the film to look up
        Returns:
          A dict containing the details for the requested film.
        """
        request = f"films/{int(film_id)}"
        return self._get(request)

    def list_persons_films(self, person_id: int) -> list:
        """
        Finds a list of films in which the person has appeared.

        Args:
          person_id: An int specifying the ID of the person whose films to look up
        Returns:
          A list containing the titles of the films in which the requested person has
              appeared.
        """
        person_info = self.find_person(person_id)
        print(f"Name: {person_info['name']}")
        films = []
        for film in person_info["films"]:
            film_info = self._get_full_url(film)
            films.append(film_info["title"])
        return films


def main():
    # Instantiate the class to an object
    obj = SWAPI()
    # Call the object's method
    luke_films = obj.list_persons_films(1)
    # Since we don't need to pass any attributes into the class for it to work, the
    # above could totally be done without instantiation by calling
    # SWAPI.find_persons_films(1), but in many cases an API wrapper will need to
    # maintain state of some sort.
    print("Films:")
    for film in luke_films:
        print(film)


# Only runs the following if the file has been explicitly called; it is ignored if the
# file has been called due to import.
if __name__ == "__main__":
    main()
