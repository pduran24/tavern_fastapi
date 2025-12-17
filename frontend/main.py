import flet as ft
from components.products_grid import ProductGrid
from components.app_header import AppHeader

def main(page: ft.Page):
    page.title = "El Dragón Verde"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.REFRESH,
        on_click=lambda _: grid_productos.cargar_datos()
    )

    header = AppHeader()
    grid_productos = ProductGrid()

    
    layout = ft.Column(
        expand=True,
        controls=[
            header,
            grid_productos
        ]
    )

    page.add(layout)

ft.app(main) 