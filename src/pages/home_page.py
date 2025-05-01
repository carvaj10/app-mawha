import flet as ft
from api.manwha_api import get_manwhas
from components.manwha_card import ManwhaCard
from components.bar_navegation import bar_navegation


class HomePage(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        bar_navegation(self.page)
        self.content = ft.Column(spacing=2, run_spacing=2)
        self.load_manwhas()
        
    def load_manwhas(self):
        manwhas = get_manwhas()
        cards = []
        slider_list = manwhas.get("data", {}).get("new_chapters", [])
        for manwha in slider_list: 
            try:
                cover_image = manwha["cover"]
                if cover_image is None or cover_image == "":
                    cover_image = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"
            except (KeyError, TypeError):
                cover_image = "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"
            cards.append(ManwhaCard(manwha["name"], 
                                    cover_image,
                                    manwha["slug"],
                                    self.page))

        self.content.controls = []

        for i in range(0, len(cards[:14]), 2):
            row = ft.Row(spacing=2, controls=cards[i:i+2], alignment=ft.MainAxisAlignment.CENTER)
            self.content.controls.append(row)
