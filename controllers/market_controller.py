class Market:
    __sold_total = 0
    __sold_items = []
    
    def list_products(self):
        pass

    def finish_buy(self):
        pass 

    @classmethod
    def get_market_log(cls):
        # total vendido, número de vendas, produtos mais vendidos etc.
        pass

    @classmethod
    def set_sale(cls, client, product, qtd):
        sale = {
            'client_name': client,
            'product': product,
            'qtd': qtd
        }

        cls.__sold_items.append(sale)
