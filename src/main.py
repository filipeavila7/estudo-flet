import flet as ft
from templates.page1 import Page1
from templates.page2 import Page2

def main(page: ft.Page):
    page.adaptive = True
    page.title = 'Meu app de Páginas'
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 500
    page.window.height = 500
    
    page.fonts = {
        'Bloody Stencil':'/fonts/bloody_stencil/Bloody Stencil.ttf',
        'Game Bubble' : '/fonts/game_bubble/Game Bubble.ttf'
    }


    def mudar_rota(e):
        if e.control.selected_index == 0:
            page.go('/')
        elif e.control.selected_index == 1:
            page.go('/tela2')
        elif e.control.selected_index == 2:
            page.go('/explore')

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.CONTACT_SUPPORT_OUTLINED, label="Contato", ),
            ft.NavigationBarDestination(icon=ft.Icons.BOOKMARK_BORDER,
                                        selected_icon=ft.Icons.BOOKMARK,
                                        label="Explore",),
        ],
        on_change=mudar_rota
    )

    def rotas(route):
        page.controls.clear()
        if route == '/':
            tela = Page1(page)
        elif route == '/tela2':
            tela = Page2(page)
        else:
            tela = Page1(page)

        page.add(tela.construir())
    
        page.update()

    page.on_route_change = lambda e: rotas(e.route)
    page.go('/')
    page.add(ft.Text("Body!"))

    page.update()

ft.app(target=main, assets_dir='assets')
