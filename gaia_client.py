import requests

class GaiaClient:
    def __init__(self, node_url):
        self.node_url = node_url

    def get_data(self, endpoint):
        response = requests.get(f"{self.node_url}/{endpoint}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    def post_data(self, endpoint, data):
        response = requests.post(f"{self.node_url}/{endpoint}", json=data)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
