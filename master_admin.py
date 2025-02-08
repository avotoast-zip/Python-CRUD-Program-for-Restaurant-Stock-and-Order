# master_admin.py details all operations that can be performed by user type = "Master Admin"

# --- IMPORTS ---

from main import *
from user import *
from messages import *

# --- FUNCTIONS --- 

def masterAdminMenu(currentUserID):
    userMenuMsg("Master Admin")
    selectActionMsg()
    option1 = printOption("1. View user(s)")
    option2 = printOption("2. Add or update user(s)")
    option3 = printOption("3. Delete user(s)")
    option4 = printOption("4. Change password")
    print("5. Logout")
    print("6. Exit program")

    # Looping until user enters a correct number
    selection = None
    while selection not in ["1","2","3","4","5","6"]:
        selection = enterSelectionMsg()

        # # # View user selection

        if selection == "1":
            print(option1)
            selectActionMsg()
            suboption1 = printOption("1. View all users")
            suboption2 = printOption("2. View specific user(s)")
            print("3. Back to main menu")

            # Looping until user enters a correct number
            subselect = None
            while subselect not in ["1","2","3"]:
                subselect = enterSelectionMsg()
                if subselect not in ["1","2","3"]:
                    invalidInputMsg()

            # View all users subselection
            if subselect == "1":
                print(suboption1)
                getUser()

                # Ask if user wants to perform another action
                moreActionConfirm(currentUserID)
            
            # View specific user(s) subselection
            elif subselect == "2":
                print(suboption2)
                query = input("Enter the user ID(s) to view separated by comma: ")
                query = query.upper().replace(" ","").split(",")

                for i in query:
                    print("")
                    getUser(i)

                # Ask if user wants to perform another action
                moreActionConfirm(currentUserID)

            # Back to main menu subselection
            elif subselect == "3":
                masterAdminMenu(currentUserID)



        # # # Add new / update user selection

        elif selection == "2":
            print(option2)
            selectActionMsg()
            suboption1 = printOption("1. Add new user")
            suboption2 = printOption("2. Update user info")
            print("3. Back to main menu")

            # Looping until user enters a correct number
            subselect = None
            while subselect not in ["1","2","3"]:
                subselect = enterSelectionMsg()
                if subselect not in ["1","2","3"]:
                    invalidInputMsg()

            # Add new user subselection
            if subselect == "1":
                print(suboption1)

                while True:

                    while True:
                        # User ID input
                        newUserID = input("Enter new user ID: ")
                        if checkUser(newUserID) == False:
                            break
                        userExistsMsg()
                        print("")

                    # User role input
                    newUserRole = selectRole()

                    # User name input
                    newUserName = input("\nEnter new user name: ")

                    # User password input
                    newUserPassword = checkPassword()

                    # Add new user
                    action = addNewUser(newUserID, newUserRole, newUserName, newUserPassword) == False
                    if userConfirmation("Add") == True:
                        continue
                    break

                #Ask if user wants to perform another action
                moreActionConfirm(currentUserID)

            # Update user info subselection
            elif subselect == "2":
                print(suboption2)
                
                while True:
                    # User ID input
                    updateUserID = input("Enter user ID: ")

                    # Display user info
                    print("")
                    getUser(updateUserID)

                    if updateUserID.upper() in appUser:

                        # Get update key
                        updateKey = input("What information(s) do you want to update? (Separated by comma)")
                        updateKey = updateKey.replace(" ","").split(",")

                        for i in range(len(updateKey)):
                            if updateKey[i] != "Role":
                                updateValue = input(f"\nEnter new value for {updateKey[i]}: ")
                            else:
                                updateValue = selectRole()
                            updateUser(currentUserID, updateUserID, updateKey[i], updateValue)
                        else:
                            if userConfirmation("Update") == True:
                                continue
                        break

                # Ask if user wants to perform another action
                moreActionConfirm(currentUserID)

            # Back to main menu subselection
            elif subselect == "3":
                masterAdminMenu(currentUserID)



        # # # Delete user selection
        elif selection == "3":
            print(option3)
            selectActionMsg()
            suboption1 = printOption("1. Delete by user ID")
            suboption2 = printOption("2. Delete all users")
            print("3. Back to main menu")

            # Looping until user enters a correct number
            subselect = None
            while subselect not in ["1","2","3"]:
                subselect = enterSelectionMsg()
                if subselect not in ["1","2","3"]:
                    invalidInputMsg()

            if subselect == "1":
                print(suboption1)
                status = False
                while status == False:
                    delete = input("\nEnter the user ID to deleted: ")
                    status = deleteUser(currentUserID, delete)

                # Ask if user wants to perform another action
                moreActionConfirm(currentUserID)

            elif subselect == "2":
                print(suboption2)
                status = deleteUser(currentUserID)

                # Ask if user wants to perform another action
                moreActionConfirm(currentUserID)



        # Change password selection
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
            masterAdminMenu(currentUserID)
            break