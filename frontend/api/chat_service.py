import requests
import json


API_URL = "http://localhost:8000/chat/" 

class ChatService:
    @staticmethod
    def send_message(message: str):
        """
        Envía el mensaje a la API.
        Nota: El backend ya se encarga de inyectar el contexto de la DB,
        así que solo necesitamos enviar el texto del usuario.
        """
        headers = {"Content-Type": "application/json"}
        
        payload = {
            "message": message
        }
        
        try:
            print(f"DEBUG: Enviando a {API_URL} -> {payload}")
            response = requests.post(API_URL, json=payload, headers=headers)
            
            if response.status_code == 200:
                # Tu router devuelve {"response": ai_reply}
                data = response.json()
                return data.get("response", "Sandyman te mira en silencio.")
            else:
                print(f"ERROR API: {response.text}")
                return f"Sandyman está ocupado (Error {response.status_code})."
                
        except requests.exceptions.ConnectionError:
            return "No se oye nada... (El servidor backend parece apagado)."
        except Exception as e:
            return f"Algo extraño ocurre: {str(e)}"