class Client:
    __cart = []

    def __init__(self, id ,name, username, password, money, admin = False):
        self.__id = id
        self.name = name 
        self.username = username
        self.__password = password
        self.__money = money
        self.__admin = admin

    def add_to_cart(self, product):
        self.__cart.append(product)

    def get_cart(self):
        return self.__cart

    def get_money(self):
        return self.__money

    def set_money(self, amount):
        self.__money += amount

    def get_client_info(self):
        return {
            'id': self.__id, 
            'name': self.name, 
            'username': self.username, 
            'money': self.__money, 
            'admin': self.__admin
        }
    
    def check_password(self, password):
        return password == self.__password
