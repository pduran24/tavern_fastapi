import flet as ft
from models.client import Client

class ClientCard(ft.Container):
    def __init__(self, client: Client, on_select_callback):
        super().__init__()
        self.client = client
        self.on_select = on_select_callback

        # Estilo base de la carta
        self.width = 150
        self.height = 180
        self.bgcolor = ft.Colors.GREY_900
        self.border = ft.border.all(2, ft.Colors.GREY_700)
        self.border_radius = 15
        self.padding = 10
        self.alignment = ft.alignment.center
        
        # Animaciones
        self.animate_scale = ft.Animation(150, ft.AnimationCurve.EASE_OUT)
        self.animate_border = ft.Animation(150, ft.AnimationCurve.EASE_OUT)
        self.on_hover = self.animar_hover
        self.on_click = lambda _: self.on_select(self.client) # Al hacer clic, enviamos el cliente al main

        # Contenido visual
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5,
            controls=[
                # Avatar (Usamos un Icono por ahora, futuro: self.client.avatar_image)
                ft.Container(
                    padding=10,
                    bgcolor=ft.Colors.BLACK54,
                    border_radius=50,
                    content=ft.Icon(ft.Icons.PERSON, size=40, color=ft.Colors.AMBER),
                ),
                ft.Container(height=5), # Espacio
                ft.Text(
                    self.client.name, 
                    size=16, 
                    weight=ft.FontWeight.BOLD, 
                    text_align=ft.TextAlign.CENTER,
                    no_wrap=True
                ),
                ft.Text(
                    f"{self.client.cash} 💰", 
                    size=14, 
                    color=ft.Colors.GREEN_400, 
                    weight=ft.FontWeight.BOLD
                ),
            ]
        )

    def animar_hover(self, e):
        """Efecto al pasar el ratón: crece y se pone dorada"""
        is_hover = e.data == "true"
        self.scale = 1.05 if is_hover else 1.0
        self.border = ft.border.all(2, ft.Colors.AMBER) if is_hover else ft.border.all(2, ft.Colors.GREY_700)
        self.bgcolor = ft.Colors.GREY_800 if is_hover else ft.Colors.GREY_900
        self.update()