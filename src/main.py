import flet as ft
from pages.home_page import HomePage
from components.safe_area import DynamicSafeArea

def main(page: ft.Page):
    page.title = "Manwhas App"
    page.scroll = "auto"
    page.add(DynamicSafeArea(HomePage(page)))

if __name__ == "__main__":
    ft.app(target=main)
