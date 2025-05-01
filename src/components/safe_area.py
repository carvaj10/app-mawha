import flet as ft

class DynamicSafeArea(ft.Container):
    def __init__(self, content):
        super().__init__(expand=True)
        self.content = content
        self.padding = None
        self.content = ft.Container(content=self.content, expand=True)
        self.controls = [self.content]

    def did_mount(self):
        is_mobile = self.page.platform in [ft.PagePlatform.ANDROID, ft.PagePlatform.IOS]
        
        padding_values = {
            "top": 40 if is_mobile else 16,
            "bottom": 24 if is_mobile else 16,
            "left": 16,
            "right": 16
        }

        print(f"Padding values: {padding_values}")

        self.content.padding = ft.padding.only(**padding_values)
        self.update()
