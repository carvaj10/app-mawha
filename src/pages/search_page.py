import flet as ft
from api.manwha_api import search_manwhas_query
from components.manwha_card import ManwhaCard

class SearchPage(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.content = ft.Column(spacing=2, run_spacing=2)
        
        self.search_title = ft.Text("Buscar Manwhas", size=24, weight=ft.FontWeight.BOLD)
        self.search_field = ft.TextField(
            label="Escribe el nombre del manwha",
            width=300,
            prefix_icon=ft.Icons.SEARCH,
            on_submit=self.search_manwhas,
        )
        
        self.results_container = ft.Column(spacing=10)
        
        self.content = ft.Column(
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.search_title,
                self.search_field,
                self.results_container
            ]
        )
    
    def search_manwhas(self, e):
        query = e.control.value
        manwhas = search_manwhas_query(query)
        cards = []
        for manwha in manwhas: 
            try:
                cover_image = manwha["cover"].replace('-sm', '-lg')
                if cover_image is None or cover_image == "":
                    cover_image = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"
            except (KeyError, TypeError):
                cover_image = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"
            cards.append(ManwhaCard(manwha["name"], 
                                    cover_image,
                                    manwha["slug"],
                                    self.page))

        self.results_container.controls = []
        
        for i in range(0, len(cards[:14]), 2):
            row = ft.Row(spacing=2, controls=cards[i:i+2], alignment=ft.MainAxisAlignment.CENTER)
            self.results_container.controls.append(row)
        
        self.update()
        print(f"Buscando: {query}, Resultados encontrados: {len(manwhas)}")