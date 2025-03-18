import flet as ft
import requests
import os

def busca_cep(e):
    input_cep.value = input_cep.value.replace('-','')
    if len(input_cep.value) != 8: #Se o CEP digitado for diferente de 8 digitos
        pass #Não faz nada
        print(len(input_cep.value)) 
    else:
        #Link da Api com o cep
        link = link = f'https://viacep.com.br/ws/{input_cep.value}/json/'
        #Requisição do cep
        requisicao = requests.get(link)
        endereço = requisicao.json()
        
        #Dados
        os.system('cls')
        if 'erro' not in endereço:
            cep = endereço['cep']
            logradouro = endereço['logradouro']
            complemento = endereço['complemento']
            uf = endereço['uf']
            bairro = endereço['bairro']
            cidade = endereço['localidade']
            regiao = endereço['regiao']
            ddd = endereço['ddd']

            #Print dos resultados
            print('\033[1;32m==> CEP ENCONTRADO <==\033[m')
            print(f'\033[1mCEP:\033[m {cep}')
            print(f'\033[1mLogadouro:\033[m {logradouro}')
            print(f'\033[1mComplemento:\033[m {complemento}')
            print(f'\033[1mUf:\033[m {uf}')
            print(f'\033[1mBairro:\033[m {bairro}')
            print(f'\033[1mCidade:\033[m {cidade}')
            print(f'\033[1mRegião:\033[m {regiao}')
            print(f'\033[1mDDD:\033[m {ddd}')

            


def main(page: ft.Page):
    global input_cep

    page.window.height = 700
    page.window.width = 650
    page.title = 'CepGo'  # Título
    page.theme_mode = ft.ThemeMode.LIGHT  # Tema claro
    page.padding = 30

    input_cep = ft.TextField(
        label='Digite o CEP',
        border_radius=20,
        expand=True
    )

    # Função para formatar o CEP enquanto o usuário digita
    def format_cep(event):
        value = input_cep.value
        # Remover caracteres não numéricos
        value = ''.join(filter(str.isdigit, value))
        # Adicionar a formatação
        if len(value) > 5:
            value = value[:5] + '-' + value[5:8]
        input_cep.value = value
        page.update()

    # Adicionar o evento de alteração de texto para o campo de CEP
    input_cep.on_change = format_cep

    btn_buscar = ft.ElevatedButton(
        text='Buscar Dados',
        icon=ft.icons.SEARCH,
        expand=True,
        on_click=busca_cep
    )

    page.add( #Adiciona elementos na página
        ft.Column( #Cria uma coluna para organizar os elementos verticalmente
            controls=[ #Define os controles que serão adicionados dentro da coluna
                ft.Text('Buscar CEP', size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_600), #Cria um texto
                ft.Divider(), #Adiciona uma linha divisoria
                ft.Container( #Cria um container para agrupar os componentes internos
                    content=ft.Column( #Dentro do container h
                        controls=[
                            ft.Text('CEP', size=16, weight=ft.FontWeight.BOLD),
                            ft.Row([input_cep, btn_buscar], alignment=ft.MainAxisAlignment.START),
                        ],
                        spacing=10
                    ),
                    padding=20,
                    border_radius=20,
                    bgcolor=ft.colors.GREY_50,
                    shadow=ft.BoxShadow(blur_radius=15, color=ft.colors.GREY_400)
                ),
            ]
        )
    )

    page.update()

ft.app(main)
