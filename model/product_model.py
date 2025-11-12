class Product:
    def __init__(self,id, name , price, stock):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_info(self):
        return (self.__name, self.__price, self.__stock)
    
    def get_stock(self):
        return self.__stock
    
    def get_product_id(self):
        return self.__id
