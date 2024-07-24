class ProductList:
    def __init__(self):
        self.__product_list = []


    def add_product(self, new_item):
        """
        Adds a new product to the shopping cart, if the product exists, increments quantity by 1
        :param new_item: product to be added
        :return: N/A
        """
        for product in self.__product_list:
            if product.get_name() == new_item.get_name() and product.get_brand() == new_item.get_brand() and product.get_barcode() == new_item.get_barcode():
                current_quantity = product.get_quantity()
                product.set_quantity(current_quantity + 1)
                return print("Incremented the quantity of {0} - {1}".format(product.get_name(), product.get_brand()))

        self.__product_list.append(new_item)

    def get_all_products(self):
        """
        :return: list of all items in shopping cart / error message if none
        """
        if len(self.__product_list) == 0:
            return print("No products in the list")
        return self.__product_list

    def get_item_position(self, barcode_to_find: str):
        """
        Returns the position of a product in the shopping cart;
        - None if the product doesn't exist -
        :param: the barcode of the product we are searching for
        :return: integer - requested position
        """

        for product in self.__product_list:
            print(self.__product_list.index(product))
            if product.get_barcode() == barcode_to_find:
                return product
        raise Exception("Product not found")

    def modify_product_data(self, item_to_modify): # NOT IMPLEMENTED
        item_position = self.get_item_position(item_to_modify)
        if item_position is None:
            return print("The item you are trying to modify does not exist")
        self.__product_list[item_position].modify_data(item_to_modify.get_name(), item_to_modify.get_quantity(),
                                                       item_to_modify.get_barcode(), item_to_modify.get_price(),
                                                       item_to_modify.get_brand())

    def get_products_from_brand(self, given_brand: str):
        brand_specific_item_list = []
        for product in self.__product_list:
            if product.get_brand() == given_brand:
                brand_specific_item_list.append(product)
        if len(brand_specific_item_list) == 0:
            return print("{0} does not have any items in this shop at the moment".format(given_brand))
        return brand_specific_item_list

    def buy_product(self, given_name, given_brand, given_quantity):
        for item in self.__product_list:
            if item.get_name() == given_name and item.get_brand() == given_brand:
                prev_quantity = item.get_quantity()
                if prev_quantity < given_quantity:
                    return print("Stock is lower than requested quantity, namely: {0}".format(prev_quantity))
                item.set_quantity(prev_quantity - given_quantity)
