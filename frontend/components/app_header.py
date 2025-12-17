import flet as ft

class AppHeader(ft.Column):
    def __init__(self):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

        self.etiqueta_tema = ft.Text("Ojo de Sauron", size = 12)

        switch_tema = ft.Switch(value=True,on_change=self.cambiar_tema)


        col_switch = ft.Column(
            controls=[self.etiqueta_tema, switch_tema],
            spacing=0, horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        fila_inicio = ft.Row(
            controls = [
                ft.Container(width=150), # izq
                ft.Container(width=300), # centro
                ft.Container(content=col_switch, padding=ft.padding.only(right=20)) #derecha
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        titulo = ft.Text("🐉Existencias🐉", size=50, weight=ft.FontWeight.BOLD, scale=1.0)
        contenedor_titulo = ft.Container (
            on_hover=self.animar_titulo,
            content=ft.Container(
                content=titulo,
                border=ft.border.all(3, ft.Colors.RED_400),
                border_radius=100,
                padding=10,
                margin=ft.margin.only(top=10, bottom=25),
                scale=1.0,
                animate_scale=ft.Animation(
                    250, ft.AnimationCurve.ELASTIC_OUT
                ),
                on_hover=self.animar_titulo
            )
        )

        fila_titulo = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                contenedor_titulo 
            ]
        )


        self.controls = [
            fila_inicio,
            fila_titulo
        ]


    def cambiar_tema(self, e):
        if e.control.value:
            e.page.theme_mode = ft.ThemeMode.DARK
            self.etiqueta_tema.value = "Ojo de Sauron"
        else:
            e.page.theme_mode = ft.ThemeMode.LIGHT
            self.etiqueta_tema.value = "Luz de Valinor"
        e.page.update()
        self.etiqueta_tema.update()

    def animar_titulo(self,e):
        if e.data == "true":
            e.control.scale = 1.05
        else:
            e.control.scale = 1.0
        e.control.update()

