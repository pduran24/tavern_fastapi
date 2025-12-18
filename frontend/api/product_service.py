import httpx
from models.product import Product

API_URL = "http://127.0.0.1:8000"

class ProductService: 
    @staticmethod
    def get_all_products():
        try:
            response = httpx.get(f"{API_URL}/products/")
            if response.status_code == 200:
                data = response.json()
                data.sort(key=lambda x: x['id']) 
                return [Product.from_json(item) for item in data]
            return []
        except Exception as e:
            print(f"Error conexión: {e}")
            return []

    # --- FUNCIÓN PARA COMPRAR ---
    @staticmethod
    def buy_product(client_id: int, product_id: int, quantity: int):
        try:
            payload = {
                "client_id": client_id,
                "product_id": product_id,
                "quantity": quantity
            }
            response = httpx.post(f"{API_URL}/transactions/buy", json=payload)
            return response
        except Exception as e:
            print(f"Error en compra: {e}")
            return None