import flet as ft

def main(page: ft.Page):
    page.theme_mode = "light"
    new_task = ft.TextField(hint_text="What needs to be done?")
    
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()
    
    page.add(
        new_task, 
        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked)
    )
    

ft.app(main)