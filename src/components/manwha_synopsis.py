import flet as ft

def ManwhaSynopsis(summary):
    return ft.Column([
        ft.Text("Sinopsis", size=18, weight="bold"),
        ft.Container(
            content=ft.Text(summary, size=16),
            border=ft.border.all(1, ft.Colors.BLACK12),
            border_radius=10,
            padding=20
        )
    ])
