import flet as ft
from api.transaction_service import TransactionService

class HistoryDialog(ft.AlertDialog):
    def __init__(self, client_id, page_ref):
        super().__init__()
        self.client_id = client_id
        self.page_ref = page_ref
        
        self.title = ft.Text("📜 Libro de Cuentas", font_family="Cinzel")
        self.bgcolor = ft.Colors.GREY_900
        
        # UI Carga
        self.content = ft.Column(
            width=400,
            height=300,
            controls=[ft.ProgressBar(color=ft.Colors.AMBER)]
        )
        # cargar datos
        self.cargar_datos()

    def cargar_datos(self):
        orders = TransactionService.get_history_by_client(self.client_id)
        
        if not orders:
            self.content = ft.Container(
                height=200,
                alignment=ft.alignment.center,
                content=ft.Text("Aún no has gastado monedas aquí.", italic=True)
            )
        else:
            lista = ft.ListView(expand=True, spacing=10, padding=10)
            for o in orders:
                # Formatear fecha  
                fecha = o['timestamp'].split("T")[0]
                hora = o['timestamp'].split("T")[1][:5]
                
                item = ft.Container(
                    padding=10,
                    border=ft.border.all(1, ft.Colors.GREY_800),
                    border_radius=10,
                    bgcolor=ft.Colors.BLACK54,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row(controls=[
                                ft.Icon(ft.Icons.RECEIPT_LONG, color=ft.Colors.AMBER, size=20),
                                ft.Column(spacing=2, controls=[
                                    ft.Text(f"Producto ID: {o['product_id']}", weight="bold", size=14),
                                    ft.Text(f"{fecha} - {hora}", size=10, color="grey")
                                ])
                            ]),
                            ft.Column(horizontal_alignment=ft.CrossAxisAlignment.END, spacing=2, controls=[
                                ft.Text(f"- {o['total_price']} 💰", color=ft.Colors.RED_200, weight="bold"),
                                ft.Text(f"Cant: {o['quantity']}", size=10)
                            ])
                        ]
                    )
                )
                lista.controls.append(item)
            
            self.content = ft.Container(width=400, height=300, content=lista)

        self.actions = [
            ft.TextButton("Cerrar Libro", on_click=self.cerrar)
        ]
        self.page_ref.update()

    def cerrar(self, e):
        self.open = False
        self.page_ref.update()