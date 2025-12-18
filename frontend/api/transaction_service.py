import httpx

API_URL = "http://127.0.0.1:8000"

class TransactionService:
    @staticmethod
    def get_history_by_client(client_id: int):
        try:
            # Pedimos todo el historial (En un sistema real filtraríamos en backend)
            response = httpx.get(f"{API_URL}/transactions/history")
            if response.status_code == 200:
                all_orders = response.json()
                # Filtramos en Python solo las de este cliente
                # Ordenamos para ver las más nuevas primero
                client_orders = [o for o in all_orders if o['client_id'] == client_id]
                client_orders.reverse() 
                return client_orders
            return []
        except Exception as e:
            print(f"Error historial: {e}")
            return []