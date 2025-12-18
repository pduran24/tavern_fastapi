import flet as ft

class AppHeader(ft.Container):
    def __init__(self, client, on_logout, on_history_click, page_ref):
        super().__init__()
        self.client = client
        self.on_logout = on_logout
        self.on_history_click = on_history_click
        self.page_ref = page_ref
        
        # Estética
        self.padding = ft.padding.symmetric(horizontal=20, vertical=15)
        self.bgcolor = ft.Colors.GREY_900
        self.border = ft.border.only(bottom=ft.BorderSide(2, ft.Colors.AMBER_900))
        self.shadow = ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK)
        
        # Elemento de Dinero
        self.txt_money = ft.Text(
            f"{self.client.cash} 💰", 
            size=20, 
            weight=ft.FontWeight.BOLD, 
            color=ft.Colors.AMBER,
            font_family="Cinzel"
        )

        self.content = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                # IZQUIERDA: Info Jugador
                ft.Row(controls=[
                    ft.Container(
                        padding=5,
                        border=ft.border.all(2, ft.Colors.AMBER),
                        border_radius=50,
                        bgcolor=ft.Colors.BLACK,
                        content=ft.Icon(ft.Icons.PERSON, color=ft.Colors.AMBER)
                    ),
                    ft.Column(spacing=0, alignment=ft.MainAxisAlignment.CENTER, controls=[
                        ft.Text(self.client.name, weight="bold", size=16),
                        ft.Text("Viajero", size=10, italic=True, color="grey")
                    ])
                ]),

                # CENTRO: Título
                ft.Row(visible=True, controls=[
                    ft.Image(src="beer.png", width=60),
                    ft.Text(" Existencias ", font_family="Cinzel", size=24, weight="bold", color=ft.Colors.WHITE),
                    ft.Image(src="beer.png", width=60),

                ]),

                # DERECHA: Dinero - Historial - Salir
                ft.Row(controls=[
                    # 1. Dinero
                    ft.Container(
                        padding=ft.padding.symmetric(horizontal=15, vertical=8),
                        bgcolor=ft.Colors.BLACK54, border_radius=10,
                        border=ft.border.all(1, ft.Colors.AMBER_900),
                        content=self.txt_money
                    ),
                    ft.Container(width=10),
                    
                    # 2. BOTÓN HISTORIAL 
                    ft.IconButton(
                        icon=ft.Icons.HISTORY_EDU, 
                        tooltip="Libro de Cuentas", 
                        icon_color=ft.Colors.AMBER_200, 
                        on_click=self.on_history_click
                    ),
                    
                    # 3. Botón Salir
                    ft.IconButton(
                        icon=ft.Icons.LOGOUT_ROUNDED, 
                        icon_color=ft.Colors.RED_400, 
                        tooltip="Salir", 
                        on_click=self.on_logout
                    )
                ])
            ]
        )

    def update_money(self, new_amount):
        self.txt_money.value = f"{new_amount} 💰"
        self.txt_money.update()