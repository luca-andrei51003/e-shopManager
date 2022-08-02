from EntityRelated.product_repository import ProductList


class AdminService:
    def __init__(self, product_list: ProductList):
        self.__product_list = product_list

    def add_product(self, new_item):
        self.__product_list.add_product(new_item)

    def get_all_products(self):
        print(self.__product_list.get_all_products())

    def get_item_position(self, barcode_to_find: str):
        self.__product_list.get_item_position()

    def get_products_from_brand(self, given_brand: str):
        self.__product_list.get_products_from_brand(given_brand)
