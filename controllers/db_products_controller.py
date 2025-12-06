import sqlite3
from model.product_model import Product

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
            with sqlite3.connect('./database/products.db') as connection:
                cursor = connection.cursor()

                data = cursor.execute('SELECT * FROM products')
                data = data.fetchall()

                products = [Product(*p) for p in data]
                return products
            
        except Exception as e:
            print('Erro ao buscar os produtos!')
            print(f'Erro: {e}')

    @classmethod
    def verify_product(cls, product):
        try:
            return next((True for p in cls.get_products() if p.get_product_info()[0].lower() == product.lower()), False)
        
        except Exception as e:
            print('Erro ao verificar os produtos.')
            print(f'Erro: {e}')

    @classmethod
    def get_product(cls, product):
        try: 
            return next((p for p in cls.get_products() if p.get_product_info()[0].lower() == product.lower()), None)

        except Exception as e:
            print('Erro ao buscar produto.')
            print(f'Erro: {e}')
