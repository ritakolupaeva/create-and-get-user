import requests

BASE_URL = "https://petstore.swagger.io/v2"


class UserAPI:

    @staticmethod
    def create_user(user_payload):
        url = f"{BASE_URL}/user/createWithList"
        return requests.post(url, json=user_payload)

    @staticmethod
    def get_user(username):
        url = f"{BASE_URL}/user/{username}"
        return requests.get(url)
    
    @staticmethod
    def delete_user(username):
        url = f"{BASE_URL}/user/{username}"
        return requests.delete(url)