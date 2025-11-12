from controllers.db_products_controller import Db_products_controller as prodController
from view import login_view
from services.session_manager import Session_manager
from model.product_model import Product
from utils.terminal import clear, sleep
import uuid

class Interface:
    pass

def create_product():
    user = Session_manager.get_client_info()
    while True:
        clear()

        print('==========> Mercado Virtual <==========')
        if not user:
            print('Nenhum usuário logado.')
            print('Voltando ao menu...')

            sleep()
            menu()

        if not user.get_client_info()['admin']:
            print('Apenas adms podem adicionar produtos.')
            sleep()
            menu()

            
        print('Informações do produto')

        product_name = input('Digite o nome do produto: ')
        product_price = input('Digite o preço do produto: ')
        product_stock = input('Digite a quantidade do produto: ')

        clear()
        
        if prodController.verify_product(product_name):
            print('Já existe um produto com esse nome.')
            sleep()
            menu()
        
        print('-----------------------------------------')
        print('Verifique as informações do produto')
        print('-----------------------------------------')
        

        if not product_name and not product_price and not product_stock:
            clear()
            print('Todos os campos devem ser preenchidos!')
            sleep()
            create_product()

        print(f'O seguinte produto será adicionado: \nNome: {product_name} \nPreço: {product_price} \nQuantidade: {product_stock}')

        print('1 - Confirmar')
        print('0 - Cancelar')
        print('-----------------------------------------')
        answer = int(input('Adicionar produto? \n---> '))
        print('-----------------------------------------')

        if answer == 1:
            clear()
            print('Cancelando adição...')
            sleep()
            menu()
            
        clear()

        product = Product(product_name, product_price, product_stock)
        prodController.set_product(product)

        sleep()
        menu()
                    
def advanced_mode():
    client_logged = Session_manager.get_client_info()

    while True:
        clear()
        print('==========> Mercado Virtual <==========')
        print('==========> Avançado')
        print('1 - Adicionar produto')
        print('2 - Ver relatório do caixa')

        if not client_logged:
            print('3 - Fazer login')

        print('0 - Voltar')

        answer = int(input('Escolha: '))

        if answer == 1:
            create_product()

        elif answer == 2:
            # Verificar se o usuário tem permissão
            pass

        elif answer == 3 and not client_logged:
            login_view.login()

        elif answer == 0:
            break

        else: 
            clear()
            print('-----------------------------------------')
            print('Não temos essa opção.')
            print('-----------------------------------------')
            sleep()

def menu():
    client_logged = Session_manager.get_client_info()

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
        if client_logged:
            print('Seja bem-vindo: ' + client_logged.name)
        else:
            print('Nenhum usuário logado!')
        print('-----------------------------------------')

        answer = int(input('Escolha: '))

        if answer == 1:
            clear()
            products = prodController.get_products()
            print('==========> Produtos <==========')
            for i, prod in enumerate(products):
                name, price, stock = prod.get_product_info()
                print(f'{i + 1} - {name} | Preço: R${price} | Quantidade: {stock}')
                print('-----------------------------------------')

            if client_logged:
                print('Deseja comprar algo?')
                answer_buy = input('1 - SIM\n2 - NÃO')

                if answer_buy == '1':
                    while True:
                        name_prod = input('Digite o nome do produto: ')
                        qtd_prod = int(input('Quantidade: '))

                        if not prodController.verify_product(name_prod):
                            clear()
                            print('Problema ao adicionar produto...')
                            sleep()
                            continue

                        buy_order = {
                            'order_id': uuid.uuid4(),
                            'product': prodController.get_product(name_prod),
                            'qtd': qtd_prod
                        }

                        client_logged.add_to_cart(buy_order)
                else:
                    clear()
                    print('Voltando...')
                    sleep()
                    menu()

            else: 
                print('Faça login para comprar algo.')
                input()

        if answer == 2:
            pass

        elif answer == 5:
            advanced_mode()

        elif answer == 0:
            clear()
            print('Saindo...')
            sleep()
            break

        else: 
            clear()
            print('-----------------------------------------')
            print('Não temos essa opção.')
            print('-----------------------------------------')
            sleep()
