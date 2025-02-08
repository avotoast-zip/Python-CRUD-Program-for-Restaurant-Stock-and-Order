# ===================================
# Restaurant Stock and Order System
# ===================================
# Developed by Cindy H. Tantowibowo (avotoast-zip)

# / --- IMPORTS --- /

import importlib
from messages import *

# / --- MAIN PROGRAM --- /

def main():

    if mainMenuMsg() == True:

        currentUser = None

        while currentUser == None:

            userID = input("\nEnter your ID: ")
            password = input("Enter your password: ")

            module = importlib.import_module("user")
            currentUser = module.getCurrentUser(userID, password)

        currentUser = str(currentUser).upper()
        userRole = module.getUser(currentUser, "Role")

        if userRole == "Master Admin":
            module = importlib.import_module("master_admin")
            module.masterAdminMenu(currentUser)
        elif userRole == "Stock Manager":
            module = importlib.import_module("stock_manager")
            module.stockManagerMenu(currentUser)
        elif userRole == "Kitchen Staff":
            module = importlib.import_module("kitchen_staff")
            module.kitchenStaffMenu(currentUser)
    
    else:
        exitMsg()



if __name__ == "__main__":
    main()