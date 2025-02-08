# kitchen_staff.py details all operations that can be performed by user type = "Kitchen Staff"

# --- IMPORTS ---

from main import *
from restomenu import *
from user import changePassword, logout
from messages import *

# --- FUNCTIONS --- 

def kitchenStaffMenu(currentUserID):
    userMenuMsg("Kitchen Staff")
    selectActionMsg()
    option1 = printOption("1. View Menu")
    option2 = printOption("2. Place Order")
    option3 = printOption("3. View Order History")
    option4 = printOption("4. Change password")
    print("5. Logout")
    print("6. Exit program")

    # Looping until user enters a correct number
    selection = None
    while selection not in ["1","2","3","4","5","6"]:
        selection = enterSelectionMsg()

        # # # View menu selection

        if selection == "1":
            print(option1)
            viewMenu()

            # Asks if user wants to perform another action
            moreActionConfirm(currentUserID)

        # # # Add new / update item selection

        elif selection == "2":
            print(option2)

            while True:
                orderID = input("Enter order ID: ")
                while True:
                    if userConfirmation("AddOrder") == True:
                        menuAdd = input("Enter menu name: ")
                        qtyAdd = input("Enter quantity: ")
                        action = placeOrder(orderID, menuAdd, qtyAdd) == True
                        continue
                    else:
                        break
                if userConfirmation("Add") == True:
                    continue
                break
        
            # Asks if user wants to perform another action
            moreActionConfirm(currentUserID)
                

        # # # View order history selection
        elif selection == "3":
            if orders != []:
                print(json.dumps(orders, indent = 3))
            else:
                noOrderHistoryMsg()

            # Asks if user wants to perform another action
            moreActionConfirm(currentUserID)

        # # # Change password selection
        elif selection == "4":
            print(option4)
            changePassword(currentUserID)

            # Ask if user wants to perform another action
            moreActionConfirm(currentUserID)



        # # # Logout selection
        
        elif selection == "5":
            selectLogout = logout()
            if selectLogout == False:
                moreActionConfirm(currentUserID)



        # # # Exit program selection

        elif selection == "6":
            if userConfirmation("Exit") == True:
                exitMsg()
            moreActionConfirm(currentUserID)



        # # # Invalid input

        if selection not in ["1","2","3","4","5","6"]:
            invalidInputMsg()


# Centralized function to allow user to perform more action by calling the main function again
def moreActionConfirm(currentUserID):
    while True:
        status = performMoreAction()
        if status == True:
            kitchenStaffMenu(currentUserID)
            break
