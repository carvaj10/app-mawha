import flet as ft
from pages.detail_page import ManwhaDetailPage  # Importamos la página de detalles

def ManwhaCard(title, image_url, slug, page):
    title = process_title(title).strip()

    def on_card_click(e):
        page.views.append(ManwhaDetailPage(title,slug))
        page.go(f"/manwha/{slug}")
        page.update()

    return ft.GestureDetector(
        on_tap=on_card_click,
        content=ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Stack([
                        ft.Container(
                            ft.Image(
                                src=image_url,
                                width=150,
                                height=200,
                                fit=ft.ImageFit.COVER
                            ),
                            alignment=ft.alignment.center,
                        ),
                    ], expand=True),
                    ft.Container(
                        ft.Text(
                            title,
                            size=14,
                            weight="bold",
                            text_align=ft.TextAlign.CENTER
                        ),
                        alignment=ft.alignment.center,
                        height=60
                    ),
                ]),
                padding=10,
                alignment=ft.alignment.center,
            ),
            elevation=0,
            variant=ft.CardVariant.OUTLINED,
            width=150,
        )
    )

def process_title(title):
    if len(title) > 20:
        return title[:20] + "..."
    return title
