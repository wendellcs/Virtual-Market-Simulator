from services.session_manager import Session_manager as session
import uuid

class Market:
    __sold_total = 0
    __sold_items = []
    
    @classmethod
    def list_products(cls):
        pass

    @classmethod
    def finish_buy(cls):
        pass 

    @classmethod
    def get_market_log(cls):
        # total vendido, número de vendas, produtos mais vendidos etc.
        pass

    @classmethod
    def set_order(cls, product, qtd):
        logged_client = session.get_client_info()
        print(product)
        print(logged_client)

        if product[2] < int(qtd):
            print('Não a quantidade disponível do seguinte produto:', product[0])
            return

        order = {
            'order_id': uuid.uuid4(),
            'client_name': logged_client.name,
            'product': product[0],
            'price': product[1],
            'qtd': qtd
        }

        logged_client.add_to_cart(order)
        print('Produto adicionado ao carrinho!')

        # cls.__sold_items.append(sale)
