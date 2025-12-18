import flet as ft
from models.product import Product

class ProductCard(ft.Container):
    def __init__(self, product: Product, on_click_callback):
        super().__init__()
        self.product = product
        self.on_click_callback = on_click_callback # Función que abre el modal

        self.bgcolor = ft.Colors.GREY_900
        self.border = ft.border.all(1, ft.Colors.GREY_800)
        self.border_radius = 15
        self.padding = 15
        self.animate_scale = ft.Animation(100, ft.AnimationCurve.EASE_OUT)
        
        # Eventos
        def on_card_clicked(e):
            print(f"DEBUG: Click en carta {self.product.name}")
            self.on_click_callback(self.product)

        self.on_click = on_card_clicked
        
        self.on_hover = self.animar_hover
        
        # Icono según categoría
        icono = "🍺"
        if self.product.category == "Comida": icono = "🍗"
        elif self.product.category == "Otros": icono = "🎒"

        # Definir color del stock
        color_stock = ft.Colors.GREY
        if self.product.stock == 0: color_stock = ft.Colors.RED
        elif self.product.stock < 5: color_stock = ft.Colors.ORANGE

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                # Parte superior: Icono y Nombre
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
                    controls=[
                        ft.Text(icono, size=40),
                        ft.Container(height=5),
                        ft.Text(
                            product.name, 
                            weight="bold", 
                            size=14, 
                            text_align="center", 
                            max_lines=2, 
                            overflow=ft.TextOverflow.ELLIPSIS
                        ),
                    ]
                ),
                
                # Parte inferior: Precio y Stock
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    controls=[
                        ft.Text(f"{product.price} 💰", color=ft.Colors.AMBER, weight="bold", size=16),
                        ft.Text(f"Stock: {product.stock}", size=11, color=color_stock)
                    ]
                )
            ]
        )

    def animar_hover(self, e):
        """efecto levantar carta"""
        is_hover = e.data == "true"
        self.scale = 1.05 if is_hover else 1.0
        self.bgcolor = ft.Colors.GREY_800 if is_hover else ft.Colors.GREY_900
        self.border = ft.border.all(1, ft.Colors.AMBER) if is_hover else ft.border.all(1, ft.Colors.GREY_800)
        self.update()