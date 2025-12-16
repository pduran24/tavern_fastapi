import flet as ft
import httpx

# Configuración
API_URL = "http://127.0.0.1:8000"

def main(page: ft.Page):
    page.title = "El Dragón Verde"
    is_dark = page.theme_mode == ft.ThemeMode.DARK
    etiqueta_tema = ft.Text("Ojo de Sauron", size=12)


    def animar_titulo_hover(e):
        if e.data == "true":
            e.control.scale = 1.1
            e.transition = 1
        else:
            e.control.scale = 1.0
        e.control.update()

    def animar_tarjeta_hover(e):
        if e.data == "true":
            e.control.scale = 1.03        
            e.transition = 1
        else:
            e.control.scale = 1.0
            e.control.bgcolor = ft.Colors.BLACK

        e.control.update()

    def cambiar_tema(e):
        if e.control.value == True:
            page.theme_mode = ft.ThemeMode.DARK
            etiqueta_tema.value = "Ojo de Sauron"
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            etiqueta_tema.value = "Luz de Valinor"
        page.update()
    
    boton_tema = ft.Switch(
        value=True,
        on_change=cambiar_tema
    )

    columna_switch = ft.Column(
        controls=[
            etiqueta_tema,
            boton_tema
        ],
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    contenedor_switch_ajustado = ft.Container(
        content=columna_switch,
        padding=ft.padding.only(right=15)
    )
    
    # Título de la página
    titulo = ft.Text("🐉Existencias🐉", size=50, weight="bold")

    caja_titulo = ft.Container(
        content=titulo,
        border=ft.border.all(3, ft.Colors.RED_400),
        border_radius=100,
        padding=10,
        margin=ft.margin.only(top=10, bottom=25),
        on_hover=animar_titulo_hover,
        animate_scale=ft.Animation(250, ft.AnimationCurve.ELASTIC_OUT),
    )

    espacio_izquierda = ft.Container(width=150)
    espacio_centro = ft.Container(width=300)

    fila_inicio = ft.Row(
        controls=[
            espacio_izquierda,
            espacio_centro,
            contenedor_switch_ajustado
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN

    )

    fila_titulo = ft.Row(
        controls=[
            caja_titulo
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    header_column = ft.Column(controls=[fila_inicio, fila_titulo])

    products_grid = ft.GridView(
        expand=1,
        runs_count=4,
        max_extent=300,
        child_aspect_ratio=0.8,
        spacing=10,
        run_spacing=10,
        padding=20
    )
    

    page.add(
        ft.Column(
            controls=[
                header_column,
                products_grid
            ],
            expand=True
        )
    )

    # Función para traer los datos del Backend
    def cargar_productos():
        try:
            print(f"Intentando conectar a: {API_URL}/products") # DEBUG 1
            
            # 1. Hacemos la petición HTTP
            response = httpx.get(f"{API_URL}/products/")
            
            print(f"Respuesta recibida: {response.status_code}") # DEBUG 2
            
            # 2. Si todo va bien (Código 200)
            if response.status_code == 200:
                print("Datos recibidos:", response.json()) # DEBUG 3
                productos = response.json()
                
                products_grid.controls.clear()

                for prod in productos:
                    icono = ft.Icons.LOCAL_DRINK if prod['category'] == "bebida" else ft.Icons.BAKERY_DINING
                    
                    tarjeta = ft.Container(
                        bgcolor=ft.Colors.BLACK,
                        border_radius=10,
                        padding=5,
                        content=ft.Container(
                            padding=10,
                            
                            content=ft.Column(
                                controls=[
                                    ft.Icon(icono, size=40, color=ft.Colors.AMBER),
                                    ft.Text(prod['name'], size=16, weight="bold", no_wrap=True, text_align="center"), 
                                    ft.Text(prod['description'] or "Sin descripción", size=12, text_align="center", color=ft.Colors.ON_SURFACE_VARIANT),
                                    ft.Divider(height=10, color="transparent"), # Espacio invisible
                                    ft.Row(
                                        [
                                            ft.Text(f"{prod['price']} 💰", size=14, weight="bold"),
                                            ft.Text(f"Stock: {prod['stock']}", size=12, color=ft.Colors.GREY),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=5
                            )
                        ),
                        on_hover=animar_tarjeta_hover,
                        animate_scale=ft.Animation(250, ft.AnimationCurve.ELASTIC_OUT),
                        border=ft.border.all(3, ft.Colors.WHITE),
                        
                    )
                    products_grid.controls.append(tarjeta)

                page.update()
            else:
                error_msg = f"Error {response.status_code}: {response.text}"
                print(error_msg)
                page.add(ft.Text(error_msg, color="red"))
                page.update()
        
        except Exception as e:
            error_conn = f"Error de conexión EXCEPCION: {e}"
            print(error_conn)
            page.add(ft.Text(error_conn, color="red"))
            page.update()

    # Llamamos a la función al iniciar
    cargar_productos()

    # Botón para recargar 
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.REFRESH, on_click=lambda _: cargar_productos()
    )

# Arrancar la app de escritorio
ft.app(target=main)