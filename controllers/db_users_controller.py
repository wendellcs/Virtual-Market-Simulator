import sqlite3
from utils.terminal import sleep
from model.client_model import Client

class Db_users_controller:
    @classmethod
    def set_client(cls, client):
        try:
            with sqlite3.connect('./database/users.db') as connection:
                cursor = connection.cursor()

                cursor.execute("""
                    INSERT INTO users (name, username, password)
                    VALUES (? , ? , ?)
                """, client)

                connection.commit()

            print('Usuário adicionado com sucesso!')
            sleep()

        except Exception as e:
            print('Ops... Parece que algo deu errado.')
            print('Encontramos um problema ao realizar o cadastro')
            print(e)
            sleep()

    @classmethod
    def get_clients(cls):
        try:
            with sqlite3.connect('./database/users.db') as connection:
                connection = sqlite3.connect('./database/users.db')
                cursor = connection.cursor()

                data = cursor.execute('SELECT * FROM users')
                data = data.fetchall()

                client_list = [Client(*c) for c in data]

                return client_list
        except: 
            print('Ocorreu um erro ao recuperar os dados.')
            sleep()

    @classmethod
    def get_client_by_username(cls, username):
        return next((c for c in cls.get_clients() if c.username == username), None)

    @classmethod
    def verify_username(cls, username):
        return next((True for c in cls.get_clients() if c.username == username), False)