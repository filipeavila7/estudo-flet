import flet as ft  # Importa a biblioteca flet para criar a interface gráfica
from templates.page1 import Page1  # Importa a classe Page1 de templates.page1
from templates.page2 import Page2  # Importa a classe Page2 de templates.page2

def main(page: ft.Page):  # Define a função principal que recebe a página como parâmetro
    page.adaptive = True  # Torna a página adaptável a diferentes tamanhos de tela
    page.title = 'Meu app de Páginas'  # Define o título da página
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER  # Alinha os controles ao centro horizontalmente
    page.theme_mode = ft.ThemeMode.LIGHT  # Define o modo de tema como claro
    page.window.width = 500  # Define a largura da janela da aplicação
    page.window.height = 500  # Define a altura da janela da aplicação
    
    # Registra fontes personalizadas para a aplicação
    page.fonts = {
        'Bloody Stencil': '/fonts/bloody_stencil/Bloody Stencil.ttf',
        'Game Bubble': '/fonts/game_bubble/Game Bubble.ttf'
    }

    def mudar_rota(e):  # Função chamada quando há mudança na seleção da barra de navegação
        if e.control.selected_index == 0:  # Se o item selecionado for o primeiro (Home)
            page.go('/')  # Navega para a página inicial (Home)
        elif e.control.selected_index == 1:  # Se o item selecionado for o segundo (Contato)
            page.go('/tela2')  # Navega para a página de Contato
        elif e.control.selected_index == 2:  # Se o item selecionado for o terceiro (Explore)
            page.go('/explore')  # Navega para a página de Explore

    # Cria a barra de navegação com três destinos
    page.navigation_bar = ft.NavigationBar(
        destinations=[  # Destinos que aparecerão na barra de navegação
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),  # Ícone e rótulo para "Home"
            ft.NavigationBarDestination(icon=ft.Icons.CONTACT_SUPPORT_OUTLINED, label="Contato"),  # Ícone e rótulo para "Contato"
            ft.NavigationBarDestination(icon=ft.Icons.BOOKMARK_BORDER,
                                        selected_icon=ft.Icons.BOOKMARK,
                                        label="Explore"),  # Ícone e rótulo para "Explore"
        ],
        on_change=mudar_rota  # Define que a função mudar_rota será chamada ao mudar a seleção
    )

    def rotas(route):  # Função para definir qual página será exibida dependendo da rota
        page.controls.clear()  # Limpa todos os controles da página antes de adicionar os novos
        if route == '/':  # Se a rota for '/' (Home)
            tela = Page1(page)  # Instancia a página 1 (Home)
        elif route == '/tela2':  # Se a rota for '/tela2' (Contato)
            tela = Page2(page)  # Instancia a página 2 (Contato)
        else:  # Se a rota for qualquer outra
            tela = Page1(page)  # Instancia a página 1 como fallback

        page.add(tela.construir())  # Adiciona a tela à página
        page.update()  # Atualiza a interface para refletir as mudanças

    # Quando a rota mudar, chama a função rotas passando a nova rota
    page.on_route_change = lambda e: rotas(e.route)
    
    page.go('/')  # Inicia a navegação para a página inicial (Home)
    page.add(ft.Text("Body!"))  # Adiciona um texto "Body!" à página (pode ser temporário)
    page.update()  # Atualiza a interface após adicionar o texto

# Inicializa o aplicativo com a função main como entrada principal e especifica o diretório de assets
ft.app(target=main, assets_dir='assets')
