import string


class Product:
    def __init__(self, name: str, quantity: int, barcode: str, price: int, brand: str):
        self.__name = name
        self.__quantity = quantity
        self.__barcode = barcode
        self.__price = price
        self.__brand = brand

    def modify_data(self, name, quantity, barcode, price, brand):
        self.__name = name
        self.__quantity = quantity
        self.__barcode = barcode
        self.__price = price
        self.__brand = brand
# Getters below

    def get_name(self):
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def get_barcode(self):
        return self.__barcode

    def get_price(self):
        return self.__price

    def get_brand(self):
        return self.__brand
# Setters below

    def set_name(self, new_name):
        self.__name = new_name

    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity

    def set_barcode(self, new_barcode):
        self.__barcode = new_barcode

    def set_price(self, new_price):
        self.__price = new_price

    def set_brand(self, new_brand):
        self.__brand = new_brand

    def __str__(self):
        return "Name: {0}, quantity: {1}, barcode: {2}, price: {3}, brand: {4} \n".format(self.__name, self.__quantity, self.__barcode, self.__price, self.__brand)

    def __repr__(self):
        return str(self)