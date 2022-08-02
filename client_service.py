from EntityRelated.item import Product
from EntityRelated.product_repository import ProductList


class ClientService:
    def __init__(self, product_repo: ProductList):
        self.__shopping_cart = []
        self.__product_list = product_repo

    def add_product_to_shopping_cart(self, new_item: Product):
        self.__shopping_cart.append(new_item) # NOT USED

    def get_shopping_cart(self):
        if len(self.__shopping_cart):
            raise ValueError("No products in your cart!")
        return self.__shopping_cart #NOT USED

    def view_all_stock(self):
        print(self.__product_list.get_all_products())

    def view_items_from_brand(self, given_brand):
        print(self.__product_list.get_products_from_brand(given_brand))

    def buy_product(self, given_name, given_brand, given_quantity):

        self.__product_list.buy_product(given_name, given_brand, given_quantity)

