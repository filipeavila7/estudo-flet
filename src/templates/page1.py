import flet as ft  # Importa a biblioteca flet para criar a interface gráfica

class Page1:  # Define a classe Page1
    def __init__(self, page: ft.Page):  # Construtor da classe, recebe a página como parâmetro
        self.page = page  # Armazena a referência da página no atributo da instância
        self.imagem = ft.Image(src='/img/logo.jpg', height=300, width=300)  # Cria um objeto de imagem, com caminho '/img/logo.jpg', altura 300px e largura 300px

    def construir(self):  # Método que cria e retorna os controles da página
        return ft.Column([  # Cria uma coluna vertical com os controles
            ft.Text('Bem vindo a tela 1!', font_family='Bloody Stencil', size=30),  # Adiciona um texto de boas-vindas com fonte personalizada e tamanho 30
            ft.Row(  # Cria uma linha horizontal para dispor os controles lado a lado
            [
                ft.Container(  # Primeiro container, com texto não clicável
                    content=ft.Text("Non clickable"),  # Adiciona um texto dentro do container
                    margin=10,  # Define a margem ao redor do container
                    padding=10,  # Define o preenchimento interno do container
                    alignment=ft.alignment.center,  # Alinha o conteúdo ao centro dentro do container
                    bgcolor=ft.Colors.AMBER,  # Define o fundo como a cor âmbar
                    width=150,  # Define a largura do container
                    height=150,  # Define a altura do container
                    border_radius=50,  # Define o raio das bordas para deixá-las arredondadas
                ),
                self.imagem,  # A imagem criada no início é adicionada aqui
               
                ft.Container(  # Segundo container, com texto clicável mas sem efeito "Ink"
                    content=ft.Text("Clickable without Ink"),  # Adiciona um texto indicando que o container é clicável sem efeito "Ink"
                    margin=10,  # Define a margem ao redor do container
                    padding=10,  # Define o preenchimento interno do container
                    alignment=ft.alignment.center,  # Alinha o conteúdo ao centro dentro do container
                    bgcolor=ft.Colors.GREEN_200,  # Define o fundo como a cor verde clara
                    width=150,  # Define a largura do container
                    height=150,  # Define a altura do container
                    border_radius=10,  # Define o raio das bordas para deixá-las arredondadas
                    on_click=lambda e: print("Clickable without Ink clicked!"),  # Adiciona uma função de clique, que imprime no console quando o container é clicado
                ),
               
                ft.Container(  # Terceiro container, com texto clicável e com efeito "Ink"
                    content=ft.Text("Clickable transparent with Ink"),  # Adiciona um texto indicando que o container é clicável com efeito "Ink"
                    margin=10,  # Define a margem ao redor do container
                    padding=10,  # Define o preenchimento interno do container
                    alignment=ft.alignment.center,  # Alinha o conteúdo ao centro dentro do container
                    width=150,  # Define a largura do container
                    height=150,  # Define a altura do container
                    border_radius=10,  # Define o raio das bordas para deixá-las arredondadas
                    ink=True,  # Habilita o efeito "Ink", que mostra um toque visual quando o container é clicado
                    on_click=lambda e: print("Clickable transparent with Ink clicked!"),  # Adiciona uma função de clique, que imprime no console quando o container é clicado
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Alinha os elementos na linha (Row) ao centro
        ),
        ])  # Retorna a coluna com todos os controles
