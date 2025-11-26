import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None, **kwargs):
        """
        Makes a GET request.
        
        Args:
            endpoint: API endpoint (can have {id} placeholders)
            params: Query parameters
            **kwargs: Path parameters like id=123
        """
        url = endpoint.format(**kwargs) if kwargs else endpoint
        response = requests.get(f"{self.base_url}{url}", params=params)
        return response

    def post(self, endpoint, data=None):
        response = requests.post(f"{self.base_url}{endpoint}", json=data)
        return response
    
    # Adicione métodos para PUT, DELETE, etc. conforme necessário.