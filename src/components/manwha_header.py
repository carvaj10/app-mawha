import flet as ft

def ManwhaHeader(data):
    cover_url = data.get("cover") or "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"
    name = data.get("name", "Desconocido")
    status = data.get("status", {}).get("name", "Estado desconocido")
    genres = ", ".join([genre.get("name", "") for genre in data.get("genres", [])])
    chapter_count = data.get("chapter_count", 0)

    return ft.Row([
        ft.Container(
            content=ft.Image(
                src=cover_url,
                width=200,
                height=280,
                fit=ft.ImageFit.COVER,
                border_radius=10
            ),
            margin=ft.margin.only(right=20)
        ),
        ft.Column([
            ft.Text(name, size=24, weight="bold"),
            ft.Container(height=10),
            ft.Text(f"Estado: {status}", size=16),
            ft.Text(f"Capítulos: {chapter_count}", size=16),
            ft.Container(height=10),
            ft.Text("Géneros:", size=16, weight="bold"),
            ft.Text(genres, size=14)
        ], expand=True)
    ])
