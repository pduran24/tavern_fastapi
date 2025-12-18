import flet as ft
from views.login_view import LoginView
from views.tavern_view import TavernView

def main(page: ft.Page):
    # --- CONFIGURACIÓN GLOBAL ---
    page.title = "La Taberna del Dragón Verde"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.assets_dir = "assets"
    
    # --- ESTADO DE LA APP ---
    current_client = None

    # --- ENRUTAMIENTO / NAVEGACIÓN ---
    
    def ir_al_login(e=None):
        """Limpia y carga la vista de Login"""
        nonlocal current_client
        current_client = None # reset cliente
        
        page.clean()
        # instanciar la vista pasándole el callback de éxito
        vista = LoginView(page, on_login_success=ir_a_taberna)
        page.add(vista)
        page.update()

    def ir_a_taberna(cliente_seleccionado):
        """Limpia y carga la vista de la Taberna"""
        nonlocal current_client
        current_client = cliente_seleccionado
        
        page.clean()
        # instanciar la vista pasándole el cliente y el callback de salida
        vista = TavernView(page, current_client, on_logout=ir_al_login)
        page.add(vista)
        page.update()

    # --- INICIO ---
    ir_al_login()

if __name__ == "__main__":
    ft.app(target=main)