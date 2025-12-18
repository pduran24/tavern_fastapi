import httpx
from models.client import Client
API_URL = "http://127.0.0.1:8000"

class ClientService:
    @staticmethod
    def get_all_clients():
        try:
            response=httpx.get(f"{API_URL}/clients/")
            if response.status_code==200:
                data=response.json()
                return [Client.from_json(item) for item in data]
        except Exception as e:
            print(f"Error de conexion: {e}")
            return []
