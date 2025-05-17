import flet as ft
from api.manwha_api import get_manwha_details, get_manwha_chapters, get_manwha_chapters_quantity
from pages.chapters_page import ChapterPage
from components.manwha_header import ManwhaHeader
from components.manwha_synopsis import ManwhaSynopsis
from components.manwha_chapters_list import ManwhaChaptersList

class ManwhaDetailPage(ft.View):
    def __init__(self, title, slug):
        self.slug = slug
        self.chapters_to_show = 30
        self._load_data()
        self.all_chapters = self.manwha_chapters.copy()
        self.data_cop = self.data.copy() if self.data is not None else None

        super().__init__(
            scroll=ft.ScrollMode.AUTO,
            route=f"/manwha/{slug}",
            controls=[
                ft.AppBar(
                    title=ft.Text(title),
                    bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
                    leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=self.go_back)
                ),
                ft.Container(
                    content=self.build_detail_content(),
                    padding=10
                )
            ]
        )

    def _load_data(self):
        self.data = get_manwha_details(self.slug)
        self.manwha_count_chapters = get_manwha_chapters_quantity(self.slug)
        self.manwha_chapters = get_manwha_chapters(self.slug, int(self.manwha_count_chapters['last_page']))

    def open_chapter(self, chapter):
        chapter_page = ChapterPage(
            slug=self.slug,
            chapter_id=chapter.get("id"),
            chapter_name=chapter.get("name"),
            manwha_name=self.data_cop.get("name", "Desconocido") if self.data_cop else "Desconocido",
        )
        if self.page is not None and self.page.views is not None:
            self.page.views.append(chapter_page)
            self.page.update()

    def load_more_chapters(self, e):
        self.chapters_to_show += 30
        container = self.controls[1]
        container.content = self.build_detail_content()
        self.update()

    def go_back(self, e):
        if self.page is not None and self.page.views is not None:
            if len(self.page.views) > 1:
                self.page.views.pop()
                self.page.update()

    def build_detail_content(self):
        displayed_chapters = self.all_chapters[:self.chapters_to_show]

        return ft.Column(
            controls=[
                ManwhaHeader(self.data_cop),
                ft.Container(height=20),
                ManwhaSynopsis(self.data_cop.get("summary", "Sin descripción") if self.data_cop else "Sin descripción"),
                ManwhaChaptersList(displayed_chapters, self.chapters_to_show, len(self.all_chapters), self.open_chapter, self.load_more_chapters)
            ],
            spacing=10,
            scroll=ft.ScrollMode.AUTO
        )
