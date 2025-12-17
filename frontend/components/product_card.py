import flet as ft
from models.product import Product

class ProductCard(ft.Container):
    def __init__(self, product: Product):
        super().__init__()
        self.product = product

        self.bgcolor = ft.Colors.BLACK
        self.border = ft.border.all(3, ft.Colors.WHITE)
        self.border_radius = 10
        self.padding = 10
        self.scale = 1.0
        self.animate_scale = ft.Animation(250, ft.AnimationCurve.ELASTIC_OUT)
        self.on_hover = self.animar_card

        icono = "🍻"
        if self.product.category == "Comida":
            icono = "🍗"
        elif self.product.category == "Otros":
            icono = "🧭"

        self.content = ft.Container(
            padding=10,
            content=ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
                controls=[
                    ft.Text(
                        product.name,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.WHITE
                    ),
                    ft.Container(
                        expand=True,
                        content=ft.Column(
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    icono,
                                    size=45
                                ),
                                ft.Text(
                                    product.description,
                                    size=12,
                                    text_align=ft.TextAlign.CENTER,
                                    color=ft.Colors.ON_SURFACE_VARIANT
                                )
                            ],
                        )
                    ),
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                    ft.Row(
                        controls=(
                            ft.Text(f"{product.price} 💰", size=14, weight=ft.FontWeight.BOLD),
                            ft.Text(product.stock, size=12, color=ft.Colors.GREY)
                        ),
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ]
            )
        )

    def animar_card(self, e):
        if e.data == "true":
            self.scale = 1.03
            self.bgcolor = ft.Colors.with_opacity(0.35, ft.Colors.YELLOW)
        else:
            self.scale = 1.0
            self.bgcolor = ft.Colors.BLACK

        self.update()