import sqlite3
from utils.terminal import sleep

class Db_products_controller:
    @classmethod
    def set_product(self, product):
        try:
            with sqlite3.connect('./database/products.db') as connection:
                cursor = connection.cursor()

                cursor.execute("""
                    INSERT INTO products (product, price, qtd)
                    VALUES (? , ? , ?)
                """, product.get_product_info())
                
                connection.commit()

            print('Produto adicionado com sucesso!')
        except Exception as e:
            print('Erro ao adicionar produto!')
            print(f'Erro: {e}')
            
    @classmethod
    def get_products(self):
        try:
            data = None
            with sqlite3.connect('./database/products.db') as connection:
                cursor = connection.cursor()

                data = cursor.execute('SELECT * FROM products')
                data = data.fetchall()

            return data
        except Exception as e:
            print('Erro ao buscar os produtos!')
            print(f'Erro: {e}')
            sleep()

    @classmethod
    def verify_product(cls, product):
        try:
            product_list = cls.get_products()

            for p in product_list:
                if product == p[1]:
                    return True
            
            return False
        
        except Exception as e:
            print('Erro ao verificar os produtos.')
            print(f'Erro: {e}')
            sleep()
