from EntityRelated.item import Product


class SaleService:
    # NOT USED
    def __init__(self, percent, list_of_barcodes, price):
        self.__percent = percent
        self.__list_of_barcodes = list_of_barcodes = []
        self.__price = price

    def set_percentage(self, new_percentage):
        self.__percent = new_percentage

    def add_product_to_list(self, barcode_to_add):
        self.__list_of_barcodes.append(barcode_to_add)

    def update_price(self, percentage):
        old_price = product.get_price()
        self.__price = old_price - (percentage/100)*old_price
