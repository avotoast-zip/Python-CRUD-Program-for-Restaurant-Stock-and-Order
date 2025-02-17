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
    option1 = printOption("1. View Menu and Place Order")
    option3 = printOption("2. View Order History")
    option4 = printOption("3. Change password")
    print("4. Logout")
    print("5. Exit program")

    # Looping until user enters a correct number
    selection = None
    while selection not in ["1","2","3","4","5"]:
        selection = enterSelectionMsg()

        # # # View menu selection

        if selection == "1":
            print(option1)
            viewMenu()

            # Allow user to add items to order
            while True:
                if userConfirmation("AddToOrder") == True:
                    menuAdd = input("Enter menu name: ")
                    qtyAdd = input("Enter quantity: ")
                    action = placeOrder(menuAdd, qtyAdd)
                    continue
                else:
                    break

            # Asks if user wants to perform another action
            moreActionConfirm(currentUserID)


        # # # View order history selection
        elif selection == "2":
            print(option3)
            if orders != []:
                print(json.dumps(orders, indent = 3))
            else:
                noOrderHistoryMsg()

            # Asks if user wants to perform another action
            moreActionConfirm(currentUserID)

        # # # Change password selection
        elif selection == "3":
            print(option4)
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
            kitchenStaffMenu(currentUserID)
            break
