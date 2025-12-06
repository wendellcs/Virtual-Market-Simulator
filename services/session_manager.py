from controllers.db_users_controller import Db_users_controller as uController
import view.navigation as nav

class Session_manager:
    __client = None

    @classmethod
    def get_client_info(cls):
        return cls.__client
    
    @classmethod
    def set_login(cls, username):
        cls.__client = uController.get_client_by_username(username)

    @classmethod
    def validate_login_info(cls, username, password):
        return next((True for c in uController.get_clients() if c.username == username and c.check_password(password)), False)

    @classmethod
    def set_logout(cls):
        cls.__client = None

    @classmethod
    def handle_login(cls,username, password ):
        if not username or not password:
            print('Preencha todos os campos')

        response = cls.validate_login_info(username, password)

        if response:
            cls.set_login(username)
            print('Login efetuado com sucesso')
            nav.show_screen('home')

    @classmethod
    def handle_register(cls, name, username, password, repeated_password):
        if not name or not username or not password or not repeated_password:
            print('Preencha todos os campos')
            return 
        
        if password != repeated_password:
            print('As senhas são diferentes.')
            return

        user_info = (name, username, password)

        response = uController.set_client(user_info)

        if response == None:
            nav.show_screen('home')