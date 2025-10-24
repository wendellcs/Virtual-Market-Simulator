from controllers.db_products_controller import Db_products_controller as prodController
from view import login_view
from services.session_manager import Session_manager as session
from model.product_model import Product
from utils.terminal import clear, sleep

class Interface:
    pass

def create_product():
    user = session.get_client_info()
    while True:
        clear()

        print('==========> Mercado Virtual <==========')
        if user:
            if user['admin']:
                print('Informações do produto')

                product_name = input('Digite o nome do produto: ')
                product_price = input('Digite o preço do produto: ')
                product_stock = input('Digite a quantidade do produto: ')

                clear()
                
                if prodController.verify_product(product_name):
                    print('Já existe um produto com esse nome.')
                    sleep()
                    start_app()
                
                print('-----------------------------------------')
                print('Verifique as informações do produto')
                print('-----------------------------------------')
                

                if product_name and product_price and product_stock:
                    print(f'O seguinte produto será adicionado: \nNome: {product_name} \nPreço: {product_price} \nQuantidade: {product_stock}')

                    print('1 - Confirmar')
                    print('0 - Cancelar')
                    print('-----------------------------------------')
                    answer = int(input('Adicionar produto? \n---> '))
                    print('-----------------------------------------')

                    if answer == 1:
                        clear()

                        product = Product(product_name, product_price, product_stock)
                        prodController.set_product(product)

                        sleep()
                        start_app()
                    else:
                        clear()
                        print('Cancelando adição...')
                        sleep()

                        start_app()

                else: 
                    clear()
                    print('Todos os campos devem ser preenchidos!')
                    sleep()
                    create_product()

            else: 
                print('Apenas adms podem adicionar produtos.')
                sleep()
                start_app()

        else: 
            print('Nenhum usuário logado.')
            print('Voltando ao menu...')

            sleep()
            start_app()

def advanced_mode():
    while True:
        clear()
        print('==========> Mercado Virtual <==========')
        print('==========> Avançado')
        print('1 - Adicionar produto')
        print('2 - Fazer login')
        print('3 - Ver relatório do caixa')
        print('0 - Voltar')

        answer = int(input('Escolha: '))

        if answer == 1:
            create_product()

        if answer == 2:
            login_view.login()

        if answer == 3:
            # Verificar se o usuário tem permissão
            pass

        if answer == 0:
            break

def start_app():
    user = session.get_client_info()
    while True:
        clear()
        print('==========> Mercado Virtual <==========')
        print('1 - Listar produtos')
        print('2 - Adicionar ao carrinho <- Mudar essa opção')
        print('3 - Ver carrinho')
        print('4 - Finalizar compra')
        print('5 - Avançado')
        print('0 - Sair')

        print('-----------------------------------------')
        if user:
            print('Seja bem-vindo: ' + user.name)
        else:
            print('Nenhum usuário logado!')
        print('-----------------------------------------')


        client = False

        answer = int(input('Escolha: '))

        if answer == 1:
            clear()
            products = prodController.get_products()
            print('==========> Produtos <==========')
            print(products)
            print('-----------------------------------------')

            input('Envie qualquer valor para voltar: ')

        if answer == 2:
            if client:
                pass

        if answer == 5:
            advanced_mode()

        if answer == 0:
            clear()
            print('Saindo...')
            sleep()
            break
