import flet as ft

def get_error_content(message, retry_callback):
    print("Error:", message)

    return ft.Column(
        controls=[
            ft.Text("Error al cargar el capítulo", size=18),
            ft.Text(str(message), size=14, color=ft.colors.ERROR),
            ft.ElevatedButton("Reintentar", on_click=retry_callback)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )
