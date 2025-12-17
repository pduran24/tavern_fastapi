import flet as ft
from api.product_service import ProductService
from components.app_header import AppHeader

def main(page: ft.Page):
    page.title = "El Dragón Verde"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    
    
    
    page.add(AppHeader())

ft.app(main) 