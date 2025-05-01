import flet as ft

def ManwhaChaptersList(chapters, chapters_to_show, total_chapters, open_chapter, load_more_chapters):
    chapter_controls = [
        ft.Container(
            content=ft.Row([
                ft.Text(f"Capítulo {chapter['name']}", weight="bold", size=16),
                ft.Container(expand=True),
                ft.Icon(name=ft.Icons.VISIBILITY, size=16, color=ft.Colors.GREY_400)
            ]),
            padding=10,
            margin=ft.margin.symmetric(horizontal=8, vertical=2),
            border_radius=8,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            ink=True,
            on_click=lambda e, c=chapter: open_chapter(c)
        ) for chapter in chapters
    ]

    if chapters_to_show < total_chapters:
        chapter_controls.append(
            ft.Container(
                content=ft.ElevatedButton(
                    "Mostrar más capítulos",
                    icon=ft.Icons.EXPAND_MORE,
                    on_click=load_more_chapters,
                    expand=True
                ),
                margin=ft.margin.only(top=10),
                padding=ft.padding.all(5)
            )
        )

    return ft.ListView(
        expand=True,
        spacing=8,
        controls=chapter_controls
    )
