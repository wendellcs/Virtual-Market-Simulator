from controllers.db_users_controller import Db_users_controller as uController
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
