import flet as ft

class ImageViewer(ft.Column):
    def __init__(self, pages, batch_size, load_more_callback=None):
        super().__init__(
            controls=[],
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
        self.pages = pages
        self.batch_size = batch_size
        self.load_more_callback = load_more_callback
        self.current_batch = 0
        self.is_loading = False
        self.load_more_button = None
        
        self.load_next_batch()
    
    def load_next_batch(self):
        if self.is_loading:
            return
        self.is_loading = True
        
        start_idx = self.current_batch * self.batch_size
        end_idx = min(start_idx + self.batch_size, len(self.pages))
        
        for i in range(start_idx, end_idx):
            self.controls.append(
                ft.Container(
                    content=ft.Image(
                        src=self.pages[i],
                        fit=ft.ImageFit.CONTAIN,
                        width=800
                    ),
                    margin=ft.margin.only(bottom=10),
                    alignment=ft.alignment.center
                )
            )
        
        self.current_batch += 1
        self.is_loading = False
    
    def has_more(self):
        return self.current_batch * self.batch_size < len(self.pages)
