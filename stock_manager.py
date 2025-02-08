# stock_manager.py details all operations that can be performed by user type = "Stock Manager"

# --- IMPORTS ---

from main import *
from stock import *
from user import changePassword, logout
from messages import *

# --- FUNCTIONS ---

def stockManagerMenu(currentUserID):
    userMenuMsg("Stock Manager")
    selectActionMsg()
    option1 = printOption("1. View kitchen stock data")
    option2 = printOption("2. Add or update kitchen stock")
    option3 = printOption("3. Change password")
    print("4. Logout")
    print("5. Exit program")

    # Looping until user enters a correct number
    selection = None
    while selection not in ["1","2","3","4","5"]:
        selection = enterSelectionMsg()

        # # # View kitchen stock selection

        if selection == "1":
            print(option1)
            selectActionMsg()
            suboption1 = printOption("1. View all kitchen stock data")
            suboption2 = printOption("2. Check specific item stock")
            print("3. Back to main menu")

            # Looping until user enters a correct number
            subselect = None
            while subselect not in ["1","2","3"]:
                subselect = enterSelectionMsg()
                if subselect not in ["1","2","3"]:
                    invalidInputMsg()

            
            # View all kitchen stock subselection
            if subselect == "1":
                print(suboption1)
                getStock()

                # Ask if user wants to perform another action
                moreActionConfirm(currentUserID)

            # View specific item(s) subselection
            elif subselect == "2":
                print(suboption2)
                query = input("Enter the item name(s) to check separated by comma: ")
                query = query.lower().title().replace(" ","").split(",")

                for i in query:
                    print("")
                    getStock(i)

                # Ask if user wants to perform another action
                moreActionConfirm(currentUserID)

            # Back to main menu subselection
            elif subselect == "3":
                stockManagerMenu(currentUserID)

        # # # Add new / update item selection

        elif selection == "2":
            print(option2)
            selectActionMsg()
            suboption1 = printOption("1. Add new item")
            suboption2 = printOption("2. Add stock quantity")
            suboption3 = printOption("3. Reduce stock quantity")
            print("4. Back to main menu")

            # Looping until user enters a correct number
            subselect = None
            while subselect not in ["1","2","3","4"]:
                subselect = enterSelectionMsg()
                if subselect not in ["1","2","3","4"]:
                    invalidInputMsg()

            # Add new item subselection
            if subselect == "1":
                print(suboption1)

                while True:

                    while True:
                        # Item name input
                        newItemName = input("Enter new item name: ")
                        if checkStock(newItemName) == False:
                            break
                        itemExistsMsg()
                        print("")

                    # Quantity input
                    newQty = input("\nEnter new quantity: ")

                    # Add new item
                    action = addItem(newItemName, newQty) == False
                    if userConfirmation("Add") == True:
                        continue
                    break

                #Ask if user wants to perform another action
                moreActionConfirm(currentUserID)

            # Add item quantity subselection
            elif subselect == "2":
                print(suboption2)
                
                while True:

                    while True:
                        # Item name input
                        updateItemName = input("Enter item name: ")
                        if checkStock(updateItemName) == True:
                            break
                        itemNotFoundMsg()
                        print("")

                    # Display item info
                    print("")
                    getStock(updateItemName)

                    # Get quantity
                    addQty = input("Enter additional item quantity: ")
                    addStock(updateItemName.lower().title(), addQty)

                    if userConfirmation("Update") == True:
                        continue
                    break

                # Ask if user wants to perform another action
                moreActionConfirm(currentUserID)

            # Reduce item quantity subselection
            elif subselect == "3":
                print(suboption3)
                
                while True:
                    
                    while True:
                        # Item name input
                        updateItemName = input("Enter item name: ")
                        if checkStock(updateItemName) == True:
                            break
                        itemNotFoundMsg()
                        print("")

                    # Display item info
                    print("")
                    getStock(updateItemName)

                    # Get quantity
                    reduceQty = input("Enter item quantity to be reduced: ")
                    reduceStock(updateItemName.lower().title(), reduceQty)

                    if userConfirmation("Update") == True:
                        continue
                    break

                # Ask if user wants to perform another action
                moreActionConfirm(currentUserID)

            # Back to main menu subselection
            elif subselect == "4":
                stockManagerMenu(currentUserID)



        # Change password selection
        elif selection == "3":
            print(option3)
            changePassword(currentUserID)

            # Ask if user wants to perform another action
            moreActionConfirm(currentUserID)



        # # # Logout selection
        
        elif selection == "4":
            selectLogout = logout()
            if selectLogout == False:
                moreActionConfirm(currentUserID)



        # # # Exit program selection

        elif selection == "5":
            if userConfirmation("Exit") == True:
                exitMsg()
            moreActionConfirm(currentUserID)



        # # # Invalid input

        if selection not in ["1","2","3","4","5"]:
            invalidInputMsg()



# Centralized function to allow user to perform more action by calling the main function again
def moreActionConfirm(currentUserID):
    while True:
        status = performMoreAction()
        if status == True:
            stockManagerMenu(currentUserID)
            break