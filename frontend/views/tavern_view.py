import flet as ft
import threading 
from components.app_header import AppHeader
from components.products_grid import ProductGrid
from components.product_dialog import ProductDetailDialog
from components.history_dialog import HistoryDialog
from components.tavern_chat import TavernChat 
from api.product_service import ProductService
from api.chat_service import ChatService

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
        # 1. Header
        self.header = AppHeader(
            client=self.current_client, 
            on_logout=self.on_logout, 
            on_history_click=self.abrir_historial,
            page_ref=self.page_ref
        )
        
        # 2. Grid 
        self.grid = ProductGrid(on_card_click=self.abrir_modal_compra)
        contenedor_grid = ft.Container(
            content=self.grid,
            expand=4, 
            padding=ft.padding.symmetric(horizontal=10),
            bgcolor=ft.Colors.BLACK, 
            image=ft.DecorationImage(src="beer_cartel.png", fit=ft.ImageFit.COVER, opacity=0.1)
        )

        # 3. Chat
        self.chat = TavernChat(
            on_send_message=self.manejar_mensaje_chat
        )

        return [
            self.header,
            contenedor_grid,
            self.chat
        ]

    # --- LÓGICA DEL CHAT CONECTADA ---
    def manejar_mensaje_chat(self, texto):
        """
        Lógica para enviar mensaje y recibir respuesta sin congelar la UI.
        """
        # 1. Mostrar mensaje del usuario visualmente (esto ya lo hace TavernChat, pero aseguramos)
        # (El componente TavernChat ya añade el mensaje del usuario al hacer submit)
        
        # 2. Mostrar un indicador de "Pensando..."
        self.chat.agregar_mensaje("Sandyman", "...", es_ia=True)
        
        # 3. Ejecutar la petición en un hilo aparte para no bloquear la interfaz
        # Si no hacemos esto, la ventana se queda 'congelada' hasta que Ollama responda
        threading.Thread(target=self._peticion_api_segundo_plano, args=(texto,)).start()

    def _peticion_api_segundo_plano(self, texto_usuario):
        """Esta función corre en paralelo"""
        
        # Llamada a la API (puede tardar unos segundos)
        respuesta = ChatService.send_message(texto_usuario)
        
        # Como estamos en otro hilo, no podemos modificar la UI directamente.
        # Flet no es 'thread-safe' directo, pero podemos hacerlo así:
        
        # Eliminamos el mensaje de "..." (es el último de la lista)
        # Accedemos a la lista de controles del chat
        if self.chat.chat_list.controls:
            self.chat.chat_list.controls.pop() 
        
        # Añadimos la respuesta real
        self.chat.agregar_mensaje("Sandyman", respuesta, es_ia=True)
        
        # IMPORTANTE: Forzar actualización de la página desde el hilo principal
        self.page_ref.update()

    # --- ACCIONES (Igual que antes) ---
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
        # ... (Tu lógica de compra existente sin cambios) ...
        print(f"DEBUG: Comprando {quantity} de {product.name}")
        
        coste_total = round(product.price * quantity, 2)
        dinero_actual = round(self.current_client.cash, 2)

        if dinero_actual < coste_total:
            falta = round(coste_total - dinero_actual, 2)
            self.mostrar_mensaje(f"No tienes suficiente oro. Faltan {falta}.", es_error=True)
            return

        response = ProductService.buy_product(self.current_client.id, product.id, quantity)
        
        if response and response.status_code == 200:
            self.current_client.cash = round(dinero_actual - coste_total, 2)
            self.header.update_money(self.current_client.cash)
            self.grid.cargar_datos() 
            self.mostrar_mensaje(f"¡Comprado! {quantity}x {product.name}.", es_error=False)
        else:
            self.mostrar_mensaje("Error al realizar la compra.", es_error=True)

    def mostrar_mensaje(self, texto, es_error=False):
        color = ft.Colors.RED_900 if es_error else ft.Colors.GREEN_900
        icon = ft.Icons.ERROR_OUTLINE if es_error else ft.Icons.CHECK_CIRCLE_OUTLINE
        snack = ft.SnackBar(
            content=ft.Row([ft.Icon(icon, color=ft.Colors.WHITE), ft.Text(texto, color=ft.Colors.WHITE)]),
            bgcolor=color,
            behavior=ft.SnackBarBehavior.FLOATING, 
        )
        self.page_ref.open(snack)