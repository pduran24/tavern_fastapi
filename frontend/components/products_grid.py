import flet as ft
from api.product_service import ProductService
from components.product_card import ProductCard

class ProductGrid(ft.GridView):
    def __init__(self, on_card_click):
        super().__init__()
        self.on_card_click = on_card_click # guardar la función
        
        # Configuración del Grid
        self.expand = True
        self.runs_count = 4             # Columnas 
        self.max_extent = 220           # Ancho max
        self.child_aspect_ratio = 0.85  # Proporción
        self.spacing = 15
        self.run_spacing = 15
        self.padding = 10
        
        self.cargar_datos()

    def cargar_datos(self):
        """Llama a la API y regenera las cartas"""
        self.controls.clear()
        
        productos = ProductService.get_all_products()

        for p in productos:
            tarjeta = ProductCard(p, on_click_callback=self.on_card_click)
            self.controls.append(tarjeta)

        if self.page:
            self.update()