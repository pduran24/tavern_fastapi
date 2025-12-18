import flet as ft
from components.app_header import AppHeader
from components.products_grid import ProductGrid
from components.product_dialog import ProductDetailDialog
from components.history_dialog import HistoryDialog
from components.tavern_chat import TavernChat 
from api.product_service import ProductService

class TavernView(ft.Column):
    def __init__(self, page: ft.Page, current_client, on_logout):
        super().__init__()
        self.page_ref = page
        self.current_client = current_client
        self.on_logout = on_logout
        self.expand = True 
        self.spacing = 0 
        
        self.controls = self._build_ui()

    def _build_ui(self):
        self.header = AppHeader(
            client=self.current_client, 
            on_logout=self.on_logout, 
            on_history_click=self.abrir_historial,
            page_ref=self.page_ref
        )
        
        
        self.grid = ProductGrid(on_card_click=self.abrir_modal_compra)
        contenedor_grid = ft.Container(
            content=self.grid,
            expand=4, 
            padding=ft.padding.symmetric(horizontal=10),
            bgcolor=ft.Colors.BLACK, 
            image=ft.DecorationImage(src="beer_cartel.png", fit=ft.ImageFit.COVER, opacity=0.1)
        )

        # Chat
        self.chat = TavernChat(
            on_send_message=self.manejar_mensaje_chat,
        )

        return [
            self.header,
            contenedor_grid,
            self.chat
        ]

    # --- LÓGICA TEMPORAL DEL CHAT ---
    def manejar_mensaje_chat(self, texto):
        """Aquí conectaremos con la IA en el siguiente paso"""
        print(f"Chat enviado: {texto}")
        import time
        time.sleep(0.5)
        self.chat.agregar_mensaje("Sandyman", "Aún estoy limpiando jarras... ¡Dame un momento para conectarme a mi cerebro!", es_ia=True)

    # --- ACCIONES ---
    def abrir_historial(self, e):
        dialog = HistoryDialog(self.current_client.id, self.page_ref)
        self.page_ref.overlay.append(dialog)
        dialog.open = True
        self.page_ref.update()

    def abrir_modal_compra(self, product):
        dialog = ProductDetailDialog(
            product=product, 
            on_confirm_buy=self.ejecutar_compra
        )
        self.page_ref.overlay.append(dialog)
        dialog.open = True
        self.page_ref.update()

    def ejecutar_compra(self, product, quantity):
        print(f"DEBUG: Intentando comprar {quantity} de {product.name}...")
        
        # 1. Validación de Dinero
        coste_total = round(product.price * quantity, 2)
        dinero_actual = round(self.current_client.cash, 2)
        
        print(f"DEBUG: Coste: {coste_total} | Tienes: {dinero_actual}")

        if dinero_actual < coste_total:
            print("DEBUG: ¡Dinero insuficiente!")
            falta = round(coste_total - dinero_actual, 2)
            self.mostrar_mensaje(f"No tienes suficiente oro. Faltan {falta} monedas.", es_error=True)
            return

        # 2. Llamada a la API
        response = ProductService.buy_product(self.current_client.id, product.id, quantity)
        
        if response and response.status_code == 200:
            print("DEBUG: Compra ÉXITO")
            # Actualizar Dinero Local
            self.current_client.cash = round(dinero_actual - coste_total, 2)
            self.header.update_money(self.current_client.cash)
            
            # Refrescar Stock
            self.grid.cargar_datos() 
            
            # Mensaje Éxito
            self.mostrar_mensaje(f"¡Comprado! {quantity}x {product.name} añadidos.", es_error=False)
            
        else:
            print(f"DEBUG: Error API {response.status_code if response else 'None'}")
            msg = "Error de conexión"
            if response:
                try: msg = response.json().get('detail', msg)
                except: pass
            self.mostrar_mensaje(f"⚠️ {msg}", es_error=True)

    def mostrar_mensaje(self, texto, es_error=False):
        """Muestra el SnackBar usando el método moderno de Flet"""
        print(f"DEBUG: Mostrando mensaje -> {texto}")
        
        color = ft.Colors.RED_900 if es_error else ft.Colors.GREEN_900
        icon = ft.Icons.ERROR_OUTLINE if es_error else ft.Icons.CHECK_CIRCLE_OUTLINE
        
        snack = ft.SnackBar(
            content=ft.Row([
                ft.Icon(icon, color=ft.Colors.WHITE),
                ft.Text(texto, color=ft.Colors.WHITE, weight="bold")
            ]),
            bgcolor=color,
            duration=4000,
            action="Cerrar",
            action_color=ft.Colors.WHITE54,
            behavior=ft.SnackBarBehavior.FLOATING, 
        )
        
        self.page_ref.open(snack)