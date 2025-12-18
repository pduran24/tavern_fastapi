import flet as ft

class ProductDetailDialog(ft.AlertDialog):
    def __init__(self, product, on_confirm_buy):
        super().__init__()
        self.product = product
        self.on_confirm_buy = on_confirm_buy # Función que ejecutará la compra real
        self.quantity = 1
        
        # UI Elements
        self.txt_quantity = ft.Text(str(self.quantity), size=22, weight="bold", color=ft.Colors.WHITE)
        self.txt_total = ft.Text(f"Total: {self.product.price} 💰", size=18, color=ft.Colors.AMBER, weight="bold")
        self.btn_confirm = ft.ElevatedButton(
            "¡Comprar!", 
            bgcolor=ft.Colors.AMBER, 
            color=ft.Colors.BLACK,
            icon=ft.Icons.CHECK,
            on_click=self.confirmar,
            width=150
        )
        
        # Configuración del Dialog
        self.modal = True
        self.bgcolor = ft.Colors.GREY_900
        self.title = ft.Text(f"Comprar {product.name}", text_align="center", font_family="Cinzel")
        
        # Icono gigante según categoría
        icono = "🍺"
        if product.category == "Comida": icono = "🍗"
        elif product.category == "Otros": icono = "🎒"

        self.content = ft.Container(
            width=400,
            height=300,
            content=ft.Column(
                tight=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(icono, size=60),
                    ft.Text(product.description, italic=True, text_align="center", color=ft.Colors.GREY_400),
                    ft.Divider(color=ft.Colors.GREY_800),
                    
                    # Selector de Cantidad
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.IconButton(ft.Icons.REMOVE_CIRCLE_OUTLINE, icon_color=ft.Colors.RED_200, icon_size=30, on_click=self.decrement),
                            ft.Container(
                                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                border=ft.border.all(1, ft.Colors.GREY_700),
                                border_radius=10,
                                bgcolor=ft.Colors.BLACK,
                                content=self.txt_quantity
                            ),
                            ft.IconButton(ft.Icons.ADD_CIRCLE_OUTLINE, icon_color=ft.Colors.GREEN_200, icon_size=30, on_click=self.increment),
                        ]
                    ),
                    
                    ft.Container(height=10),
                    self.txt_total,
                    ft.Text(f"Stock disponible: {product.stock}", size=12, color="grey")
                ]
            )
        )
        
        self.actions = [
            ft.TextButton("Cancelar", on_click=self.close_dialog, style=ft.ButtonStyle(color=ft.Colors.GREY)),
            self.btn_confirm
        ]
        self.actions_alignment = ft.MainAxisAlignment.CENTER

    def increment(self, e):
        if self.quantity < self.product.stock:
            self.quantity += 1
            self.update_ui()

    def decrement(self, e):
        if self.quantity > 1:
            self.quantity -= 1
            self.update_ui()

    def update_ui(self):
        """Recalcula el total y actualiza la vista"""
        self.txt_quantity.value = str(self.quantity)
        total_price = round(self.product.price * self.quantity, 2)
        self.txt_total.value = f"Total: {total_price} 💰"
        self.page.update()

    def close_dialog(self, e):
        self.open = False
        self.page.update()

    def confirmar(self, e):
        self.close_dialog(e)
        # callback pasando producto y cantidad final
        self.on_confirm_buy(self.product, self.quantity)