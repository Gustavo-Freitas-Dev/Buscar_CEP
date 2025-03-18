import requests

def main():
    print()
    print('==> CONSULTAR CEP <=='.center(35)) 
    #Input CEP
    while True:
        cep = input('CEP (DIGITE 8 DIGITOS, SOMENTE NÚMERO): ')
        if len(cep) != 8:
            print('Quantidade de digitos inválida, tente novamente!')
        else:
            break 
    #Link da Api com o cep
    link = link = f'https://viacep.com.br/ws/{cep}/json/'
    #Requisição do cep
    requisicao = requests.get(link)
    endereço = requisicao.json()

    #Dados
    if 'erro' not in endereço:
        cep = endereço['cep']
        logradouro = endereço['logradouro']
        complemento = endereço['complemento']
        uf = endereço['uf']
        bairro = endereço['bairro']
        cidade = endereço['localidade']
        
        #Print dos resultados
        print('\033[1;32m==> CEP ENCONTRADO <==\033[m')
        print(f'\033[1mCEP:\033[m {cep}')
        print(f'\033[1mLogadouro:\033[m {logradouro}')
        print(f'\033[1mComplemento:\033[m {complemento}')
        print(f'\033[1mUf:\033[m {uf}')
        print(f'\033[1mBairro:\033[m {bairro}')
        print(f'\033[1mCidade:\033[m {cidade}')



    else:
        print()
        print('CEP inválido')
    print()
    nova_consulta = int(input('\033[1;31mFazer nova consulta?\033[m\n1 - Sim\n2 - Nâo\nEscolha: '))

    if nova_consulta == 1:
        main()
    elif nova_consulta == 2:
        print('\033[1;31m==> FIM DO PROGRAMA <==\033[m')

main()
