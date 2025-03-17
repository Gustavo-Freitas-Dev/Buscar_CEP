import flet as ft  # Importa a biblioteca Flet para a criação da interface gráfica

# Função principal do aplicativo
def main(page: ft.Page):
    # Define o tamanho da janela do aplicativo
    page.window.height = 700  
    page.window.width = 650  

    # Define o título da janela
    page.title = 'Busca Cep'  

    # Define o tema do aplicativo como claro
    page.theme_mode = ft.ThemeMode.LIGHT  

    # Adiciona um espaçamento interno à página
    page.padding = 30  

    # Campo de entrada para digitação do CEP
    input_cep = ft.TextField(
        label='Somente números',  # Texto indicativo dentro do campo
        border_radius=30  # Borda arredondada para um design mais moderno
    )

    # Botão de busca de CEP
    btn_buscar = ft.ElevatedButton(
        text='Buscar Dados',  # Texto do botão
        icon=ft.icons.SEARCH,  # Ícone de busca ao lado do texto
        expand=True  # Faz com que o botão ocupe todo o espaço disponível na linha
    )

    # Adiciona os elementos à página
    page.add(
        ft.Column(  # Usa uma coluna para organizar os elementos verticalmente
            controls=[ 
                # Título principal do aplicativo
                ft.Text("Buscar Cep", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_600, text_align=ft.TextAlign.CENTER),

                # Linha divisória para separação visual
                ft.Divider(),

                # Campo de entrada do CEP
                input_cep,

                # Botão de busca dentro de uma linha para melhor organização
                ft.Row([btn_buscar])
            ], 
            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza os elementos verticalmente
            spacing=20  # Define um espaçamento entre os elementos
        )
    )

    # Atualiza a interface da página
    page.update()

# Executa o aplicativo chamando a função principal
ft.app(main)
