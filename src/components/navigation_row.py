import flet as ft

def get_navigation_row(prev_chapter, next_chapter, previous_callback, next_callback):
    return ft.Row(
        controls=[
            ft.ElevatedButton(
                "Capítulo Anterior",
                icon=ft.Icons.NAVIGATE_BEFORE,
                on_click=previous_callback,
                disabled=prev_chapter is None
            ),
            ft.Container(expand=True),
            ft.ElevatedButton(
                "Capítulo Siguiente",
                icon=ft.Icons.NAVIGATE_NEXT,
                on_click=next_callback,
                disabled=next_chapter is None
            )
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
