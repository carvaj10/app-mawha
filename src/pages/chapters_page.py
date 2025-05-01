import flet as ft
from api.manwha_api import get_chapter_images
from components.loading_content import get_loading_content
from components.error_content import get_error_content
from components.image_viewer import ImageViewer
from components.navigation_row import get_navigation_row

class ChapterPage(ft.View):
    def __init__(self, slug, chapter_id, chapter_name, manwha_name):
        super().__init__(
            scroll=ft.ScrollMode.AUTO,
            route=f"/manwha/{slug}/chapter/{chapter_id}",
        )
        self.slug = slug
        self.chapter_id = chapter_id
        self.chapter_name = chapter_name
        self.manwha_name = manwha_name
        self.pages = []
        
        self.app_bar = ft.AppBar(
            title=ft.Text(f"Capítulo {chapter_name}"),
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=self.go_back),
            actions=[
                ft.IconButton(
                    icon=ft.Icons.NAVIGATE_BEFORE,
                    tooltip="Capítulo anterior",
                    on_click=self.previous_chapter,
                    disabled=True
                ),
                ft.IconButton(
                    icon=ft.Icons.NAVIGATE_NEXT,
                    tooltip="Capítulo siguiente",
                    on_click=self.next_chapter,
                    disabled=True
                ),
            ]
        )
        
        self.body_container = ft.Container(
            content=get_loading_content(),
            padding=10
        )
        
        self.controls = [self.app_bar, self.body_container]
        
        self.prev_chapter = None
        self.next_chapter = None
        
    def did_mount(self):
        self.load_chapter_data()
    
    def load_chapter_data(self):
        self.body_container.content = get_loading_content()
        self.update()
        
        try:
            data = get_chapter_images(self.slug, self.chapter_id)
            self.prev_chapter = data.get("prev_chapter")
            self.next_chapter = data.get("next_chapter")
            self.pages = data.get("chapter", {}).get("pages", [])
            
            self.app_bar.actions[0].disabled = self.prev_chapter is None
            self.app_bar.actions[1].disabled = self.next_chapter is None
            
            self.build_viewer()
            
        except Exception as e:
            self.body_container.content = get_error_content(e, self.load_chapter_data)
            self.update()
    
    def build_viewer(self):
        if not self.pages:
            self.body_container.content = get_error_content(
                self.load_chapter_data
            )
            self.update()
            return

        self.viewer = ImageViewer(self.pages, batch_size=len(self.pages))
        
        nav_row = get_navigation_row(
            self.prev_chapter,
            self.next_chapter,
            self.previous_chapter,
            self.next_chapter
        )

        controls = [
            self.viewer,
            ft.Container(height=20),
            nav_row
        ]

        self.body_container.content = ft.Column(
            controls=controls,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
        self.update()
    
    def go_back(self, e):
        if len(self.page.views) > 1:
            self.page.views.pop()
            self.page.update()
    
    def previous_chapter(self, e):
        if self.prev_chapter:
            self.navigate_to_chapter(self.prev_chapter)
    
    def next_chapter(self, e):
        if self.next_chapter:
            self.navigate_to_chapter(self.next_chapter)
    
    def navigate_to_chapter(self, chapter_info):
        page = ChapterPage(
            slug=self.slug,
            chapter_id=chapter_info.get("id"),
            chapter_name=chapter_info.get("name"),
            manwha_name=self.manwha_name
        )
        if len(self.page.views) > 1:
            self.page.views.pop()
        self.page.views.append(page)
        self.page.update()
