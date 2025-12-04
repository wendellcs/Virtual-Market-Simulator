from tkinter import *

from controllers.db_products_controller import Db_products_controller as prodController
from controllers.db_users_controller import Db_users_controller as usersCon
from services.session_manager import Session_manager as sessionMan
# from view import login_view
# from model.product_model import Product
# from utils.terminal import clear, sleep
# import uuid

root = Tk()
root.geometry('500x700')
root.title('Virtual Market')

container = Frame(root)
container.grid(row=0, column=0, sticky='nsew')

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

register_frame = Frame(container)
login_frame = Frame(container)
home_frame = Frame(container)

frames = [login_frame, register_frame, home_frame]

for frame in frames:
    frame.grid(row=0, column=0, sticky='nsew')
    frame.grid_columnconfigure(0, weight=1)

def show_screen(frame):
    frame.tkraise()

def register_view():
    show_screen(register_frame)

def login_view():
    show_screen(login_frame)

def home_view():
    show_screen(home_frame)

def handle_register(name, username, password, repeated_password):
    if not name or not username or not password or not repeated_password:
        print('Preencha todos os campos')
        return 
    
    if password != repeated_password:
        print('As senhas são diferentes.')
        return

    user_info = (name, username, password)

    response = usersCon.set_client(user_info)

    if response == None:
        home_view()

def handle_login(username, password):
    if not username or not password:
        print('Preencha todos os campos')

    response = sessionMan.validate_login_info(username, password)

    if response:
        sessionMan.set_login(username)
        print('Login efetuado com sucesso')
        home_view()

def build_login():
    title = Label(login_frame, text='Faça seu login', font=('Arial', 32, 'bold'))
    title.grid(pady=10, row=0, column=0)

    box_1 = Frame(login_frame)
    box_1.grid(row=1, column=0)

    label_1 = Label(box_1, text='Nome de usuário:')
    label_1.grid(row=0, column=0)

    entry_1 = Entry(box_1)
    entry_1.grid(row=1, column=0, ipadx=10, ipady=3)

    box_2 = Frame(login_frame)
    box_2.grid(row=2, column=0)

    label_2 = Label(box_2, text='Senha:')
    label_2.grid(row=0, column=0, pady=(10, 0))

    entry_2 = Entry(box_2)
    entry_2.grid(row=1, column=0, ipadx=10, ipady=3)

    button_1 = Button(login_frame, text='Entrar', cursor="hand2", command=lambda: handle_login(entry_1.get(), entry_2.get()))
    button_1.grid(row=3, column=0, pady=15, ipadx=30, ipady=3)

    box_3 = Frame(login_frame)
    box_3.grid(row=4, column=0)

    label_3 = Label(box_3, text='Não possui uma conta?')
    label_3.grid(row=0, column=0, pady=(10, 0))

    button_2 = Button(box_3, text='Criar uma conta', bd=0, highlightthickness=0, cursor="hand2", command=lambda:(register_view()))
    button_2.grid(row=1, column=0, pady=15, ipadx=30, ipady=3)

def build_register():
    title = Label(register_frame, text='Faça seu cadastro', font=('Arial', 32, 'bold'))
    title.grid(pady=10, row=0, column=0)

    box_1 = Frame(register_frame)
    box_1.grid(row=1, column=0)

    label_1 = Label(box_1, text='Nome:')
    label_1.grid(row=0, column=0)

    entry_1 = Entry(box_1)
    entry_1.grid(row=1, column=0, ipadx=10, ipady=3)

    box_2 = Frame(register_frame)
    box_2.grid(row=2, column=0)

    label_2 = Label(box_2, text='Nome de usuário:')
    label_2.grid(row=0, column=0)

    entry_2 = Entry(box_2)
    entry_2.grid(row=1, column=0, ipadx=10, ipady=3)

    box_3 = Frame(register_frame)
    box_3.grid(row=3, column=0)

    label_3 = Label(box_3, text='Senha:')
    label_3.grid(row=0, column=0, pady=(10, 0))

    entry_3 = Entry(box_3)
    entry_3.grid(row=1, column=0, ipadx=10, ipady=3)

    box_4 = Frame(register_frame)
    box_4.grid(row=4, column=0)

    label_4 = Label(box_4, text='Confirme sua senha:')
    label_4.grid(row=0, column=0, pady=(10, 0))

    entry_4 = Entry(box_4)
    entry_4.grid(row=1, column=0, ipadx=10, ipady=3)

    button_1 = Button(register_frame, text='Criar conta', cursor="hand2", 
                      command=lambda:handle_register(entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get()))
    
    button_1.grid(row=5, column=0, pady=15, ipadx=30, ipady=3)

    box_5 = Frame(register_frame)
    box_5.grid(row=6, column=0)

    label_4 = Label(box_5, text='Já possui uma conta?')
    label_4.grid(row=0, column=0, pady=(10, 0))

    button_2 = Button(box_5, text='Fazer login', bd=0, highlightthickness=0, cursor="hand2", command=lambda:login_view())
    button_2.grid(row=1, column=0, pady=15, ipadx=30, ipady=3)

def build_home():
    title = Label(home_frame, text='Seja bem-vindo!', font=('Arial', 32, 'bold'))
    title.grid(pady=10, row=0, column=0)

    label_1 = Label(home_frame, text='O que deseja?')
    label_1.grid(row=1, column=0)


    box_products = Frame(home_frame)
    box_products.grid(row = 2, column = 0)

    product_list = prodController.get_products()

    n_cols = 3
    for i, p in enumerate(product_list):
        r = i // n_cols
        c = i % n_cols

        product = Frame(box_products, bd=2, relief='solid')

        product.grid(row= r, column= c, padx=15, pady=10, ipadx=15)

        product_name = Label(product, text= p.get_product_info()[0])
        product_name.grid(row=0 , column=0 , sticky='w')

        product_price = Label(product, text='R$ ' + str(p.get_product_info()[1]))
        product_price.grid(row=1 , column=0 , sticky='w')

        product_stock = Label(product, text='Quantidade: ' + str(p.get_product_info()[2]))
        product_stock.grid(row=2 , column=0 , sticky='w')

        product_buttons = Frame(product)
        product_buttons.grid(row=3 , column=0, pady=10, sticky='e')

        entry_qtd = Entry(product_buttons, width=8)
        entry_qtd.grid(row=0, column=0, pady=5)

        button_buy = Button(product_buttons, text='Comprar', cursor='hand2')
        button_buy.grid(row=1 , column=0)

    box_buttons = Frame(home_frame)
    box_buttons.grid(row=3, column=0)

    button_leave = Button(box_buttons, text = 'Sair', command=root.destroy, cursor="hand2")
    button_leave.grid(row=0, column=0, pady=15, ipadx=30, ipady=3)

    button_advanced = Button(box_buttons, text = 'Avançado', cursor="hand2")
    button_advanced.grid(row=0, column=1, pady=15, ipadx=30, ipady=3)


def start_app():
    build_login()
    build_register()
    build_home()

    login_view()
    root.mainloop()


# class Interface:
#     pass

# def create_product():
#     user = Session_manager.get_client_info()
#     while True:
#         clear()

#         print('==========> Mercado Virtual <==========')
#         if not user:
#             print('Nenhum usuário logado.')
#             print('Voltando ao menu...')

#             sleep()
#             menu()

#         if not user.get_client_info()['admin']:
#             print('Apenas adms podem adicionar produtos.')
#             sleep()
#             menu()

            
#         print('Informações do produto')

#         product_name = input('Digite o nome do produto: ')
#         product_price = input('Digite o preço do produto: ')
#         product_stock = input('Digite a quantidade do produto: ')

#         clear()
        
#         if prodController.verify_product(product_name):
#             print('Já existe um produto com esse nome.')
#             sleep()
#             menu()
        
#         print('-----------------------------------------')
#         print('Verifique as informações do produto')
#         print('-----------------------------------------')
        

#         if not product_name and not product_price and not product_stock:
#             clear()
#             print('Todos os campos devem ser preenchidos!')
#             sleep()
#             create_product()

#         print(f'O seguinte produto será adicionado: \nNome: {product_name} \nPreço: {product_price} \nQuantidade: {product_stock}')

#         print('1 - Confirmar')
#         print('0 - Cancelar')
#         print('-----------------------------------------')
#         answer = int(input('Adicionar produto? \n---> '))
#         print('-----------------------------------------')

#         if answer == 1:
#             clear()
#             print('Cancelando adição...')
#             sleep()
#             menu()
            
#         clear()

#         product = Product(product_name, product_price, product_stock)
#         prodController.set_product(product)

#         sleep()
#         menu()
                    
# def advanced_mode():
#     client_logged = Session_manager.get_client_info()

#     while True:
#         clear()
#         print('==========> Mercado Virtual <==========')
#         print('==========> Avançado')
#         print('1 - Adicionar produto')
#         print('2 - Ver relatório do caixa')
#         print('3 - Gerenciar usuários')

#         if not client_logged:
#             print('4 - Fazer login')

#         print('0 - Voltar')

#         answer = int(input('Escolha: '))

#         if answer == 1:
#             create_product()

#         elif answer == 2:
#             # Verificar se o usuário tem permissão
#             pass

#         elif answer == 3:
#             user_list = userController.get_users_info(client_logged)

#             if not user_list:
#                 print('Apenas admins podem acessar essa área.')
#                 sleep()
#                 break

#             print('-----------------------------------------')
#             print('Clientes cadastrados: ')
#             for u in user_list:
#                 user_info = u.get_client_info()
#                 print(f'{user_info["id"]} - {user_info["name"]} | {user_info["username"]} | {user_info["money"]}')
#             print('-----------------------------------------')
#             print('O que gostaria de fazer?')
#             print('1 - Excluir usuário')

#             admin_answer = input('Resposta: ')

#             if admin_answer == '1':
#                 client_id = int(input('Informe o ID do cliente a ser excluído: '))
#                 userController.delete_user(client_id)

#         elif answer == 4 and not client_logged:
#             login_view.login()

#         elif answer == 0:
#             break

#         else: 
#             clear()
#             print('-----------------------------------------')
#             print('Não temos essa opção.')
#             print('-----------------------------------------')
#             sleep()

# def menu():
#     client_logged = Session_manager.get_client_info()

#     while True:
#         clear()
#         print('==========> Mercado Virtual <==========')
#         print('1 - Listar produtos')
#         print('2 - Adicionar ao carrinho <- Mudar essa opção')
#         print('3 - Ver carrinho')
#         print('4 - Finalizar compra')
#         print('5 - Avançado')
#         print('0 - Sair')

#         print('-----------------------------------------')
#         if client_logged:
#             print('Seja bem-vindo: ' + client_logged.name)
#         else:
#             print('Nenhum usuário logado!')
#         print('-----------------------------------------')

#         answer = int(input('Escolha: '))

#         if answer == 1:
#             clear()
#             products = prodController.get_products()
#             print('==========> Produtos <==========')
#             for i, prod in enumerate(products):
#                 name, price, stock = prod.get_product_info()
#                 print(f'{i + 1} - {name} | Preço: R${price} | Quantidade: {stock}')
#                 print('-----------------------------------------')

#             if client_logged:
#                 print('Deseja comprar algo?')
#                 answer_buy = input('1 - SIM\n2 - NÃO')

#                 if answer_buy == '1':
#                     while True:
#                         name_prod = input('Digite o nome do produto: ')
#                         qtd_prod = int(input('Quantidade: '))

#                         if not prodController.verify_product(name_prod):
#                             clear()
#                             print('Problema ao adicionar produto...')
#                             sleep()
#                             continue

#                         buy_order = {
#                             'order_id': uuid.uuid4(),
#                             'product': prodController.get_product(name_prod),
#                             'qtd': qtd_prod
#                         }

#                         client_logged.add_to_cart(buy_order)
#                 else:
#                     clear()
#                     print('Voltando...')
#                     sleep()
#                     menu()

#             else: 
#                 print('Faça login para comprar algo.')
#                 input()

#         if answer == 2:
#             pass

#         elif answer == 5:
#             advanced_mode()

#         elif answer == 0:
#             clear()
#             print('Saindo...')
#             sleep()
#             break

#         else: 
#             clear()
#             print('-----------------------------------------')
#             print('Não temos essa opção.')
#             print('-----------------------------------------')
#             sleep()
