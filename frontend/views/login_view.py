import flet as ft
from api.client_service import ClientService
from components.client_card import ClientCard
from components.tavern_carousel import TavernCarousel

class LoginView(ft.Container):
    def __init__(self, page: ft.Page, on_login_success):
        super().__init__()
        self.page_ref = page
        self.on_login_success = on_login_success 
        
        self.expand = True
        self.bgcolor = ft.Colors.BLACK
        # Fondo con opacidad para que resalte la UI
        self.image = ft.DecorationImage(src="beer_cartel.png", fit=ft.ImageFit.COVER, opacity=0.4)
        
        self.content = self._build_ui()

    def _build_ui(self):
        # 1. Datos
        lista_clientes = ClientService.get_all_clients()
        
        # 2. Componentes
        carousel = TavernCarousel(self.page_ref)
        
        
        texto_seleccion = ft.Container(
            width=800, # Que coincida con el ancho del grid
            padding=ft.padding.symmetric(vertical=10),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Divider(height=1, color=ft.Colors.AMBER_400),
                    ft.Icon(ft.Icons.PERSON_SEARCH, color=ft.Colors.AMBER),
                    ft.Text(
                        " SELECCIONA UN PERSONAJE ", 
                        size=20, 
                        font_family="Cinzel", 
                        color=ft.Colors.AMBER_200, 
                        weight=ft.FontWeight.BOLD
                    ),
                    ft.Icon(ft.Icons.PERSON_SEARCH, color=ft.Colors.AMBER),
                    ft.Divider(height=1, color=ft.Colors.AMBER_400),
                ]
            )
        )
        
        # --- B) GRID DE CLIENTES ---
        grid_clientes = ft.GridView(
            expand=True, 
            runs_count= 3,             # 3 columnas
            max_extent=250,           # Ancho max por carta
            child_aspect_ratio=0.85,  # Relación de aspecto
            spacing=15,               # Espacio horizontal entre cartas
            run_spacing=15,           # Espacio vertical entre cartas
            padding=20,               # Relleno interno para que no toquen el borde
        )
        
        for c in lista_clientes:
            grid_clientes.controls.append(ClientCard(client=c, on_select_callback=self.on_login_success))
        
        contenedor_clientes = ft.Container(
            content=grid_clientes,
            border=ft.border.all(2, ft.Colors.AMBER_700), # Borde más fino pero intenso
            border_radius=15,
            bgcolor=ft.Colors.with_opacity(0.85, ft.Colors.BLACK), # Fondo semi-opaco para leer bien
            height=400,  
            width=800,
            padding=10, 
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.Colors.AMBER_900,
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            )
        )

        titulo_row = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Image(src="green_dragon.png", width=60), 
                ft.Text("El Dragón Verde", size=45, weight="bold", font_family="Cinzel", color=ft.Colors.AMBER),
                ft.Image(src="green_dragon_left.png", width=60)
            ]
        )

        contenedor_titulo = ft.Container(
            content=ft.Container(
                content=titulo_row,
                border=ft.border.all(3, ft.Colors.AMBER), border_radius=100, padding=10,
                scale=1.0, animate_scale=ft.Animation(300, ft.AnimationCurve.ELASTIC_OUT),
                on_hover=self._animar_titulo
            ),
            margin=ft.margin.only(top=20, bottom=10), 
        )

        return ft.Column(
            alignment=ft.MainAxisAlignment.START, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO, 
            controls=[
                ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[contenedor_titulo]),
                carousel,
                ft.Container(height=10), # Espaciador
                texto_seleccion,
                contenedor_clientes,
                ft.Container(height=20) 
            ]
        )

    def _animar_titulo(self, e):
        e.control.scale = 1.1 if e.data == "true" else 1.0
        e.control.update()