import flet as ft
import time

class TavernCarousel(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page_ref = page # Guardamos referencia a la página para el update global
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        
        # --- CONFIGURACIÓN ---
        self.image_urls = [
            "carousel/tavern_1.png", "carousel/tavern_2.png", 
            "carousel/tavern_3.png", "carousel/tavern_4.png", 
            "carousel/tavern_5.png", "carousel/tavern_6.png",
        ]
        self.total = len(self.image_urls)
        self.current_index = 0
        self.active_view_idx = 0
        self.anim_spec = ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT_CUBIC)

        # --- VISTAS ---
        self.view_1 = ft.Container(
            content=self.build_image_row(self.current_index),
            offset=ft.Offset(0, 0),
            animate_offset=self.anim_spec,
        )
        self.view_2 = ft.Container(
            content=None,
            offset=ft.Offset(1.5, 0),
            animate_offset=self.anim_spec,
        )
        self.views = [self.view_1, self.view_2]

        # --- STACK (Viewport) ---
        self.viewport = ft.Stack(
            controls=[self.view_1, self.view_2],
            clip_behavior=ft.ClipBehavior.HARD_EDGE, 
            height=350,
        )

        # --- CONTROLES FINALES ---
        self.controls = [
            ft.Container(height=20),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.IconButton(ft.Icons.ARROW_BACK_IOS_NEW, icon_size=40, on_click=self.prev_slide),
                    ft.Container(content=self.viewport, width=850, height=300),
                    ft.IconButton(ft.Icons.ARROW_FORWARD_IOS, icon_size=40, on_click=self.next_slide),
                ]
            )
        ]

    def build_image_row(self, start_index):
        idx_left = start_index % self.total
        idx_right = (start_index + 1) % self.total
        return ft.Row(
            controls=[
                ft.Image(src=self.image_urls[idx_left], border_radius=12, fit=ft.ImageFit.COVER, expand=1, height=350),
                ft.Image(src=self.image_urls[idx_right], border_radius=12, fit=ft.ImageFit.COVER, expand=1, height=350),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        )

    def animate_transition(self, new_index, direction):
        outgoing_idx = self.active_view_idx
        incoming_idx = 1 - outgoing_idx
        
        outgoing_view = self.views[outgoing_idx]
        incoming_view = self.views[incoming_idx]

        if direction == "next":
            start_x, end_x = 1.5, -1.5
        else:
            start_x, end_x = -1.5, 1.5

        # 1. Preparar la entrada (oculta)
        incoming_view.animate_offset = None 
        incoming_view.offset = ft.Offset(start_x, 0)
        incoming_view.content = self.build_image_row(new_index)
        self.update() # Actualizamos el componente localmente
        time.sleep(0.02) 

        # 2. Animar el deslizamiento
        incoming_view.animate_offset = self.anim_spec
        outgoing_view.offset = ft.Offset(end_x, 0)
        incoming_view.offset = ft.Offset(0, 0)
        
        self.active_view_idx = incoming_idx
        self.current_index = new_index
        self.update()

    def next_slide(self, e):
        new_idx = (self.current_index + 1) % self.total
        self.animate_transition(new_idx, "next")

    def prev_slide(self, e):
        new_idx = (self.current_index - 1 + self.total) % self.total
        self.animate_transition(new_idx, "prev")