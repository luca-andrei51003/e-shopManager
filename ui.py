import string

from Services.admin_service import AdminService
from EntityRelated.item import Product
from Services.client_service import ClientService
from Services.sale_service import SaleService


class UI:
    def __init__(self, ad_service: AdminService, cl_service: ClientService):
        self.__service = ad_service
        self.__cservice = cl_service

    def modify_item(self):
        desired_barcode = input("What item do you want to modify (provide barcode below):'\n'")
        product_to_be_modified = self.__service.get_item_position(desired_barcode)
        print("Enter new product information: ")
        new_name = str(input("Change name (reintroduce previous name should you avoid changing it) : "))
        new_quantity = int(input("Update quantity: "))
        new_barcode = str(input("Change barcode: "))
        new_price = int(input("Change price: "))
        new_brand = str(input("Change brand: "))
        product_to_be_modified.set_name(new_name)
        product_to_be_modified.set_quantity(new_quantity)
        product_to_be_modified.set_barcode(new_barcode)
        product_to_be_modified.set_price(new_price)
        product_to_be_modified.set_brand(new_brand)

    def __print_admin_menu(self):
        print("1. Add new product")
        print("2. Delete product")
        print("3. Modify product")
        print("4. View all available stock")
        print("5. View stock from specific brand")
        print("6. Add new sale")

    def __print_client_menu(self):
        print("1. View all stock")
        print("2. View stock from a specific brand")
        print("3. Buy")
        print("4. View your shopping cart cart")
        print("5. Sort items by price [ provide maximum cost ]")

    def admin_run(self):
        while True:
            try:
                command = int(input("Proceed [ 1 ], back [ 0 ]: "))
                if command == 1:
                    self.__print_admin_menu()
                    admin_command = int(input("Select option: "))
                    if admin_command == 1:
                        new_product_name = str(input("Product name: "))
                        new_product_quantity = int(input("What is the stock you wish to make available? "))
                        new_product_barcode = string.ascii_letters
                        #str(input("State a barcode for the product: "))
                        new_product_price = int(input("What price will this item sell for? "))
                        new_product_brand = str(input("State the producer of this product: "))
                        new_product = Product(new_product_name, new_product_quantity, new_product_barcode,
                                              new_product_price, new_product_brand)
                        self.__service.add_product(new_product)
                    if admin_command == 2:
                        # barcode = str(input("What is the barcode of the item you wish to delete?"))
                        # item_to_delete = self.__service.get_item_position(barcode)
                        # self.__service.delete_product(item_to_delete)
                        print("SORRY, NOT SOLVED [ yet ]")
                    if admin_command == 3:
                        # searched_barcode = str(input("What is the barcode of the item you wish to update?"))
                        # item_to_modify = self.__service.get_item_position(searched_barcode)
                        # self.__service.modify_product_data(item_to_modify)
                        print("SORRY, NOT SOLVED [ yet ]")
                    if admin_command == 4:
                        # stock = self.__service.get_all_products()
                        # print('\n')
                        # for item in stock:
                        #    print(item)
                        # print('\n')
                        print(self.__service.get_all_products())
                    if admin_command == 5:
                        searched_brand = str(input("What brand do you want to display?"))
                        print(self.__service.get_products_from_brand(searched_brand))
                    if admin_command == 6:
                        sale_barcode = str(input("Barcode and brand of product"))
                        sale_product = self.__service.get_item_position(sale_barcode)

                elif command == 0:
                    break

            except ValueError:
                print("Error: option must be either 1, 2 or 0")

    def client_run(self):
        while True:
            try:
                command = int(input("Proceed [ 1 ], back [ 0 ]: "))
                if command == 1:
                    self.__print_client_menu()
                    client_command = int(input("Select option: "))
                    if client_command == 1:
                        print(self.__cservice.view_all_stock())
                    if client_command == 2:
                        print(self.__cservice.view_items_from_brand(
                            str(input("Choose the brand you want to display: "))))
                    if client_command == 3:
                        prod_name = str(input("Name of product you wish to buy: "))
                        prod_brand = str(input("Brand of product you wish to buy: "))
                        qty_to_buy = int(input("Quantity of product you wish to buy: "))
                        self.__cservice.buy_product(prod_name, prod_brand, qty_to_buy)
                    if client_command == 4:
                        print(self.__cservice.get_shopping_cart())
                    if client_command == 5:
                        print("SORRY, NOT SOLVED YET [ yet ]")
                elif command == 0:
                    break
            except ValueError:
                print("Error: option must be either 1, 2 or 0")
