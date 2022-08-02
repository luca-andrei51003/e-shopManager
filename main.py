from ui import UI
from Services.admin_service import AdminService
from Services.client_service import ClientService
from EntityRelated.product_repository import ProductList

product_list = ProductList()
ad_service = AdminService(product_list)
cl_service = ClientService(product_list)
ui = UI(ad_service, cl_service)
while True:
    print("1. Admin Mode - manage store")
    print("2. Client Mode - buy stuff from store")
    print("0. EXIT APP")
    command = int(input("Choose option: "))
    if command == 1:
        ui.admin_run()
    if command == 2:
        ui.client_run()
    if command == 0:
        break
