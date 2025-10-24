from controllers.db_users_controller import Db_users_controller as uController
from services.session_manager import Session_manager
from model.client_model import Client
from view.interface import start_app
import time
from utils.terminal import clear, sleep

def login():
    while True:
        clear()
        print('==========> Faça seu login <==========')

        print('-----------------------------------------')

        print('Não possui um cadastro?')
        print('1 - Cadastrar')
        print('0 - Continuar com o login')

        answer = int(input('Escolha: '))

        if answer == 1:
            register()

        clear()
        print('-----------------------------------------')

        print('Tenho cadastro!')

        client_username = input('Usuário: ')
        client_password = input('Senha: ')

        print('-----------------------------------------')

        if client_password and client_username:
            validated_client_login = Session_manager.validate_login_info(client_username, client_password)
            if validated_client_login:
                Session_manager.set_login(client_username)
                
                print('Login efetuado com sucesso!')
                print('Voltando ao menu...')
                
                sleep()
                start_app()
            else:
                print('Algo deu errado.')
                print('Confira suas informações e faça login novamente.')
                sleep()

        if answer == 0:
            clear()
            print('Voltando...')
            break


def register():
    clear()
    print('==========> Faça seu cadastro <==========')
    client_name = input('Digite seu nome: ')
    client_username = input('Crie um nome de usuário: ')
    client_password = input('Crie uma senha: ')

    clear()
    print('-----------------------------------------')
    print('Informações enviadas!')
    print('Aguarde enquanto criamos sua conta.')
    print('-----------------------------------------')

    sleep()

    try:
        if client_name and client_password and client_username:
            if uController.verify_username(client_username):
                clear()
                uController.set_client((client_name, client_username, client_password))

                print('-----------------------------------------')
                print('Faça login para continuar utilizando nossos serviços')
                print('-----------------------------------------')

                input('Envie qualquer valor para continuar com o login: ')

                login()
            else: 
                print('Usuário indisponível...')
                sleep()
        else: 
            print('Por favor preencha todos os campos.')
            sleep()
    except:
        print('-----------------------------------------')
        print('Tivemos algum problema ao criar seu login.')
        print('Tente novamente')
        print('-----------------------------------------')
        sleep()