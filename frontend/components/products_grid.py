import flet as ft
from api.product_service import ProductService
from components.product_card import ProductCard

class ProductGrid(ft.GridView):
    def __init__(self):
        super().__init__()
        self.expand = 1
        self.runs_count = 4
        self.max_extent = 300
        self.child_aspect_ratio = 0.8
        self.spacing = 10
        self.run_spacing = 10
        self.padding = 20
        
        # Cargamos los datos al iniciar (o podrías llamarlo manualmente desde main)
        self.cargar_datos()

    def cargar_datos(self):
        self.controls.clear()

        productos = ProductService.get_all_products()

        for p in productos:
            tarjeta = ProductCard(p)
            self.controls.append(tarjeta)

        if self.page:
            self.update()



