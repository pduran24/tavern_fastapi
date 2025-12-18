import flet as ft

class TavernChat(ft.Container):
    def __init__(self, on_send_message):
        super().__init__()
        self.on_send_message = on_send_message
        
        # Estética del contenedor del chat
        self.height = 700 # Altura fija para el chat
        self.bgcolor = ft.Colors.GREY_900
        self.border = ft.border.only(top=ft.BorderSide(2, ft.Colors.AMBER_900))
        self.padding = 10
        
        # 1. Área de Mensajes 
        self.chat_list = ft.ListView(
            expand=True,
            spacing=10,
            auto_scroll=True,
        )
        
        
        self.agregar_mensaje("Sandyman", "¡Bienvenido a mi barra! Pide lo que quieras, viajero.", es_ia=True)

        # 2. Campo de Texto 
        self.txt_input = ft.TextField(
            hint_text="Habla con Sandyman o pide una cerveza...",
            hint_style=ft.TextStyle(color=ft.Colors.GREY_500),
            text_style=ft.TextStyle(color=ft.Colors.WHITE),
            border_color=ft.Colors.AMBER_900,
            cursor_color=ft.Colors.AMBER,
            expand=True,
            on_submit=self.enviar_texto, # Enviar al pulsar Enter
            height=45,
            content_padding=10
        )

        # 3. Botón de Enviar
        self.btn_send = ft.IconButton(
            icon=ft.Icons.SEND_ROUNDED,
            icon_color=ft.Colors.AMBER,
            tooltip="Enviar mensaje",
            on_click=self.enviar_texto
        )

        # 4. Estructura Final
        self.content = ft.Column(
            spacing=5,
            controls=[
                # Título pequeñito del chat
                ft.Text("💬 Hablando con Sandyman", size=10, color="grey", italic=True),
                
                # Lista de mensajes (ocupa el espacio disponible dentro del contenedor de 200px)
                ft.Container(
                    content=self.chat_list,
                    expand=True, 
                    bgcolor=ft.Colors.BLACK26,
                    border_radius=5,
                    padding=5
                ),
                
                # Fila de Input + Botón
                ft.Row(
                    controls=[
                        self.txt_input,
                        self.btn_send
                    ]
                )
            ]
        )

    def agregar_mensaje(self, autor, texto, es_ia=False):
        """Método visual para pintar un globo de chat"""
        color_fondo = ft.Colors.BLUE_GREY_900 if es_ia else ft.Colors.AMBER_900
        alineacion = ft.MainAxisAlignment.START if es_ia else ft.MainAxisAlignment.END
        color_texto = ft.Colors.WHITE if es_ia else ft.Colors.BLACK
        avatar = "man.png" if es_ia else "person.png"
        
        # Creamos el globo del mensaje
        burbuja = ft.Container(
            padding=10,
            border_radius=10,
            bgcolor=color_fondo,
            content=ft.Column(
                spacing=0,
                controls=[
                    ft.Text(autor, size=10, weight="bold", color=ft.Colors.WHITE54 if es_ia else ft.Colors.BLACK54),
                    ft.Text(texto, color=color_texto)
                ]
            ),
            # Ancho máximo para textos largos, None para cortos
            width=None if len(texto) < 50 else 300 
        )

        fila = ft.Row(
            controls=[
                ft.Image(avatar, width=100) if es_ia else ft.Container(),
                burbuja,
                ft.Image(avatar, width=100) if not es_ia else ft.Container(),
            ],
            alignment=alineacion,
            vertical_alignment=ft.CrossAxisAlignment.START
        )
        
        self.chat_list.controls.append(fila)
        
        # --- CORRECCIÓN ---
        # Solo actualizamos si el componente ya está montado en la página.
        # Esto evita el error "Control must be added to the page first" durante el __init__
        if self.page:
            self.update()

    def enviar_texto(self, e):
        texto = self.txt_input.value
        if texto:
            # 1. Pintamos nuestro mensaje
            self.agregar_mensaje("Tú", texto, es_ia=False)
            
            # 2. Limpiamos input
            self.txt_input.value = ""
            self.txt_input.focus()
            self.update()
            
            # 3. Llamamos al callback (lógica futura)
            self.on_send_message(texto)