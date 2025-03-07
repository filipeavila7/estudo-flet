import flet as ft  # Importa a biblioteca flet para criar a interface gráfica

class Page2:  # Define a classe Page2
    def __init__(self, page: ft.Page):  # Construtor da classe, recebe a página como parâmetro
        self.page = page  # Armazena a referência da página no atributo da instância
        
    def construir(self):  # Método que cria e retorna os controles da página
        def button_clicked(e):  # Função chamada quando o botão é clicado
            t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."  # Atualiza o texto t com os valores dos campos de texto
            self.page.update()  # Atualiza a interface após a mudança do texto

        t = ft.Text()  # Cria um controle de texto vazio, que será usado para exibir os valores dos campos
        tb1 = ft.TextField(label="Standard")  # Cria um campo de texto padrão com o rótulo "Standard"
        tb2 = ft.TextField(label="Disabled", disabled=True, value="First name")  # Cria um campo de texto desabilitado com valor padrão "First name"
        tb3 = ft.TextField(label="Read-only", read_only=True, value="Last name")  # Cria um campo de texto somente leitura com valor padrão "Last name"
        tb4 = ft.TextField(label="With placeholder", hint_text="Please enter text here")  # Cria um campo de texto com um placeholder (dica) que aparece até o usuário digitar algo
        tb5 = ft.TextField(label="With an icon", icon=ft.Icons.EMOJI_EMOTIONS)  # Cria um campo de texto com um ícone de emoji ao lado

        b = ft.ElevatedButton(text="Submit", on_click=button_clicked)  # Cria um botão elevado com o texto "Submit", que chama a função `button_clicked` quando clicado
        
        # Retorna uma coluna com todos os componentes, incluindo texto, campos de texto e o botão
        return ft.Column([
            ft.Text('Bem vindo a tela 2!', font_family='Game bubble', size=30),  # Texto de boas-vindas com uma fonte personalizada
            t,  # Adiciona o controle de texto (t) que exibirá os valores dos campos de texto
            tb1,  # Adiciona o campo de texto padrão
            tb2,  # Adiciona o campo de texto desabilitado
            tb3,  # Adiciona o campo de texto somente leitura
            tb4,  # Adiciona o campo de texto com placeholder
            tb5,  # Adiciona o campo de texto com ícone
            b  # Adiciona o botão de envio
        ])
