# messages.py details all messages to be displayed to user

# --- IMPORTS --- 

from colorama import Fore

# --- PROMPTS ---

# Main menu message
def mainMenuMsg():
    print(Fore.WHITE + "\n================================")
    print("UNCLE TJONG'S CHINESE RESTAURANT")
    print("================================")
    print("")
    print("Welcome!")

    return userConfirmation("Login")


# User confirmation to go back to main menu
def performMoreAction():

    userConfirm = input(Fore.YELLOW + "\nPerform more action? [Y/N] " + Fore.WHITE)

    if userConfirm.capitalize() == "Y":
        return True
    
    elif userConfirm.capitalize() == "N":
        exitMsg()
    
    else:
        invalidInputMsg()
        return False

# User confirmation to perform an action
def userConfirmation(actionType = "Regular"):

    userConfirm = None

    while userConfirm not in [True, False]:
        # Define confirmation messages for different action types
        if actionType == "Regular":
            message = "\nAre you sure you want to perform this action? [Y/N] "
        elif actionType == "Login":
            message = "\nLogin to your account? [Y: Login, N: Cancel/Exit program] "
        elif actionType == "Logout":
            message = "\nAre you sure you want to logout? [Y/N] "
        elif actionType == "Exit":
            message = "\nAre you sure you want to exit the program? [Y/N] "
        elif actionType == "Add":
            message = "\nDo you want to add another? [Y/N] "
        elif actionType == "AddOrder":
            message = "\nDo you want to add item to the order? [Y/N] "
        elif actionType == "Update":
            message = "\nDo you want to update another? [Y/N] "
        elif actionType == "Delete":
            message = "\nAre you sure you want to perform deletion? [Y/N] "
        elif actionType == "Fatal":
            message = "This action is irreversible and will affect the whole program.\nAre you sure you want to perform this action? [Y/N] "

        # Ask for user confirmation
        userConfirm = input(Fore.YELLOW + message + Fore.WHITE)

        # Conditional statements
        if userConfirm.capitalize() == "Y":
            userConfirm = True
        
        elif userConfirm.capitalize() == "N":
            actionCancelledMsg()
            userConfirm = False
        
        else:
            invalidInputMsg()

    return userConfirm




# --- PRINTED MESSAGES ---

# General messages

def printOption(option):
    print(option)
    return f"\n{option}"

def enterSelectionMsg():
    return(input(Fore.WHITE + "\nEnter your selection: "))
    
def updateSuccessMsg(value):
    print(Fore.GREEN + f"\nSuccessfully updated {value}." + Fore.WHITE)

def updateFailMsg(value):
    print(Fore.RED + f"\nFailed to update {value}." + Fore.WHITE)

def invalidInputMsg():
    print(Fore.RED + "Invalid input." + Fore.WHITE)

def dataNotFoundMsg():
    print(Fore.RED + "Data not found." + Fore.WHITE)

def deleteSuccessMsg():
    print(Fore.GREEN + "Successfully deleted data." + Fore.WHITE)

def deleteAllSuccessMsg():
    print(Fore.GREEN + "Successfully deleted all data." + Fore.WHITE)

def noPermissionMsg():
    print(Fore.RED + "You do not have permission to perform this action." + Fore.WHITE)
    
def selectActionMsg():
    print(Fore.WHITE + "\nPlease select an action:")
    
def notAvailableMsg(value):
    print(Fore.RED + f"{value} is not available for update." + Fore.WHITE)
    
def actionCancelledMsg():
    print(Fore.GREEN + "Cancelled." + Fore.WHITE)


# User management messages

def loginSuccessMsg(userID, userRole):
    print(Fore.GREEN + f"\nSuccessfully logged in as {userID}: {userRole}.\n" + Fore.WHITE)

def loginFailMsg():
    print(Fore. RED + "Wrong username or password." + Fore.WHITE)

def logoutSuccessMsg():
    print(Fore.GREEN + "Logout successful." + Fore.WHITE)

def userNotFoundMsg(user=""):
    print(Fore.RED + f"User {user.upper()}not found." + Fore.WHITE)

def selfDeletionMsg():
    print(Fore.YELLOW + "You are not allowed to delete your own account." + Fore.WHITE)

def userMenuMsg(userType):
    acceptedTypes = ["Master Admin", "Stock Manager", "Kitchen Staff"]
    if userType in acceptedTypes:
        print(Fore.WHITE + "=================================")
        print(f"\nWelcome to the {userType} main menu.")

def passwordChangeSuccessMsg():
    print(Fore.GREEN + "Password successfully changed." + Fore.WHITE)

def passwordMismatchMsg():
    print(Fore.RED + "Password does not match." + Fore.WHITE)

def addUserSuccessMsg():
    print(Fore.GREEN + "User successfully added." + Fore.WHITE)

def userExistsMsg():
    print(Fore.RED + "User already exists." + Fore.WHITE)

# Stock management messages

def itemNotFoundMsg(item=""):
    print(Fore.RED + f"Item {item.lower().title()}not found." + Fore.WHITE)

def invalidQtyMsg():
    print(Fore.RED + "Quantity input has to be a number more than zero." + Fore.WHITE)

def stockNotEnoughMsg():
    print(Fore.RED + "Not enough stock." + Fore.WHITE)

def itemExistsMsg():
    print(Fore.RED + "Item already exists." + Fore.WHITE)

def addItemSuccessMsg():
    print(Fore.GREEN + "Item successfully added." + Fore.WHITE)

def currentStockMsg(qty):
    print(Fore.YELLOW + f"Current stock: {qty}" + Fore.WHITE)

# Kitchen management messages

def orderSuccessMsg(item):
    print(Fore.GREEN + f"Successfully ordered{item}." + Fore.WHITE)

def invalidIngredientMsg():
    print(Fore.RED + "Ingredient does not exist." + Fore.WHITE)

def noOrderHistoryMsg():
    print(Fore.BLUE + "There is no order history." + Fore.WHITE)

def restoMenuMsg():
    print(Fore.WHITE + "\n==============")
    print("UNCLE TJONG'S MENU")
    print("==============\n")

# Exit message

def exitMsg():
    print("\n================================")
    print("Thank you for using our system!")
    print("================================\n")
    exit()
