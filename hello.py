import flet as ft

def main(page: ft.Page):
    page.theme_mode = "light"
    page.title = "Flet Counter Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        txt_number.update()
    
    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        txt_number.update()
    
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    

ft.app(main)