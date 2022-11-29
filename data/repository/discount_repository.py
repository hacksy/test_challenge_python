"""Repositories module."""

from requests.exceptions import ConnectionError
import requests


class DiscountRepository:
    def __init__(self) -> None:
        self.default_discount = 10

    def get_discount(self) -> float:
        """ Retrieves a random discount using an api call or sets a default discount"""
        try:
            response = requests.get('https://www.randomnumberapi.com/api/v1.0/random?min=0&max=100&count=1')
            if response.status_code == 200:
                discount = int(response.text.replace("[", "").replace("]", ""))
                if 100 >= discount >= 0:
                    return discount
                else:
                    return self.default_discount
            else:
                return self.default_discount
        except (ConnectionError, ValueError) as error:
            return self.default_discount
