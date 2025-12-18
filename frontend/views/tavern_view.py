import flet as ft
from components.app_header import AppHeader
from components.products_grid import ProductGrid

class TavernView(ft.Column):
    def __init__(self, page: ft.Page, current_client, on_logout):
        super().__init__()
        self.page_ref = page
        self.current_client = current_client
        self.on_logout = on_logout
        self.expand = True
        
        self.controls = self._build_ui()

    def _build_ui(self):
        # Header
        # NOTA: en 4.2 -> pasar el current client al header reeal
        header = AppHeader() 
        
        # Botón Temporal Logout 
        btn_logout_temp = ft.ElevatedButton(
            "Salir", icon=ft.Icons.LOGOUT, 
            bgcolor=ft.Colors.RED_900, color=ft.Colors.WHITE,
            on_click=self.on_logout
        )

        # Grid
        grid = ProductGrid()

        return [
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER, 
                controls=[header, ft.Container(content=btn_logout_temp, padding=10)]
            ),
            grid
        ]