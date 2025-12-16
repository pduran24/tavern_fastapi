import httpx
from models.product import Product

API_URL = "http://127.0.0.1:8000"

class ProductService: 
    @staticmethod
    def get_all_products():
        try:
            response = httpx.get(f"{API_URL}/products/")
            if response.status_code==200:
                data = response.json()
                return [Product.from_json(item) for item in data]
            print(f"Error API: {response.status_code}")
            return []
        except Exception as e:
            print(f"Error de conexion: {e}")
            return []
