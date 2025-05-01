import flet as ft

def get_loading_content():
    return ft.Column(
        controls=[
            ft.ProgressRing(),
            ft.Container(height=10),
            ft.Text("Cargando capítulo...", size=16)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )
