import requests
import configuration
from data import order


def create_order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_URL, json=order)
    return response.status_code, response.json()


def get_order(track):
    response = requests.get(f"{configuration.URL_SERVICE}{configuration.NUMBER_URL}{track}")
    return response.status_code, response.json()


