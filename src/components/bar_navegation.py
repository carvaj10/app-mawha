import flet as ft


def bar_navegation(page: ft.Page):
    
    def on_change(e):
        selected_index = e.control.selected_index
        if selected_index == 0:
            page.go("/home")
        page.update()
    
    bar_navegation = ft.NavigationBar(
        selected_index=0,
        on_change=on_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.icons.SEARCH, label="Search"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Settings"),
        ]
    )
    
    page.add(bar_navegation)