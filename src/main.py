import flet as ft
from pages.home_page import HomePage
from components.safe_area import DynamicSafeArea
from pages.search_page import SearchPage

def main(page: ft.Page):
    page.title = "Manwhas App"
    page.scroll = ft.ScrollMode.AUTO
    
    def handle_nav_change(e):
        if e.control.selected_index == 0:
            page.controls = [DynamicSafeArea(HomePage(page))]
        elif e.control.selected_index == 1:
            page.controls = [DynamicSafeArea(SearchPage(page))]
        elif e.control.selected_index == 2:
            page.controls = [ft.Text("Bookmark!")]
        page.update()
        
    page.navigation_bar = ft.NavigationBar(
        on_change=handle_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Search"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings"),
        ],
    )
    
    page.add(DynamicSafeArea(HomePage(page)))

if __name__ == "__main__":
    ft.app(target=main)
