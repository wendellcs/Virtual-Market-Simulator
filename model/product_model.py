from controllers.db_products_controller import Db_products_controller as pController

class Product:
    def __init__(self, name , price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_product_info(self):
        return (self.name, self.price, self.stock)
