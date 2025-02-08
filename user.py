# user.py details all user-related data and functions

# --- IMPORTS --- #

import json
import importlib
from messages import *

# --- DATA --- #

# Dictionary "appUser" defines user data for verification purposes
#   User type "Master Admin" can create, read, update, and delete user except for himself
#   User type "Stock Manager" can check, add, update, and delete kitchen stock
#   User type "Kitchen Staff" can view the restaurant menu and register food orders based on the menu

appUser = {
    "USER001" : {
        "Role" : "Master Admin",
        "Name" : "Admin",
        "Password" : "12345"
    },
    "USER002" : {
        "Role" : "Stock Manager",
        "Name" : "Ali",
        "Password" : "abcde"
    },
    "USER003" : {
        "Role" : "Kitchen Staff",
        "Name" : "Budi",
        "Password" : "abc123"
    }}

# --- FUNCTIONS --- #

# 1. Login and Get Current User

def getCurrentUser(userID=str, password=str) :

    # Define login function
    def login(loginUserID=str, loginPassword=str):
        if loginUserID.upper() in appUser:
            if (appUser[loginUserID.upper()]["Password"] == loginPassword):
                loginSuccessMsg(loginUserID.upper(), getUser(loginUserID, "Role"))
                return True
            else:
                loginFailMsg()
                return False
        else:
            loginFailMsg()

    if (login(userID, password)) == True:
        return userID

    else:
        return None

# 2. Check User Existence Function

def checkUser(userID=str):
    if userID.upper() in appUser:
        return True
    else:
        return False

# 3. Get User Function

def getUser(userID="All", info="All"):

    if (userID.upper() in appUser) or (userID == "All"):

        if info == "All":

            if userID == "All":
                print(json.dumps(appUser, indent = 3))

            else:
                # Hide password from output
                hiddenData = {"Password"}
                userData = {key:value for key, value in appUser[userID.upper()].items() if key not in hiddenData}
                print(f"User ID: {userID.upper()} {json.dumps(userData, indent = 3)}")

        else:
            if info.lower().title() in appUser[userID.upper()].keys():
                if info == "Password":
                    noPermissionMsg()
                else:
                    return appUser[userID.upper()][info.lower().title()]
            else:
                dataNotFoundMsg()

    else:
        userNotFoundMsg(str(userID) + " ")

# 4. Update User Function

def updateUser(currentUser=str, userID=str, key=str, newValue=str):
    if userID.upper() in appUser:

        # Cannot update password
        condition1 = key.lower().title() in ["Role", "Name"]
        if condition1 == False:
            notAvailableMsg(key.lower().title())

        # User is not trying to change their own role
        condition3 = not(currentUser.upper() == userID.upper() and key.lower().title() == "Role")
        if condition3 == False:
            noPermissionMsg()

        if condition1 and condition3:
            if userConfirmation() == True:
                appUser[userID.upper()][key.lower().title()] = newValue
                updateSuccessMsg(key.lower().title())
        else:
            updateFailMsg(key.lower().title())

# 5. Add New User Function

def addNewUser(userID=str, role=str, name=str, password=str):
    userID = userID.replace(" ","").upper()
    if userID not in appUser:
        appUser[userID.upper()] = {}
        appUser[userID.upper()]["Role"] = role
        appUser[userID.upper()]["Name"] = name
        appUser[userID.upper()]["Password"] = password
        addUserSuccessMsg()
        return True
    else:
        userExistsMsg()
        return False

# 6. Delete User Function

def deleteUser(currentUser, deleteUserID="All"):
    
    if deleteUserID == "All":
        if userConfirmation("Fatal") == True:
            toBeDeleted = [user for user in appUser if user != currentUser.upper()] # Create a new list without current user
            for i in toBeDeleted:
                appUser.pop(i) # Delete every user except for the current user
            deleteAllSuccessMsg()
            return True
        else:
            return False
    
    if deleteUserID.upper() == currentUser.upper():
        selfDeletionMsg()
        return False
    
    if (userConfirmation() == True):
        appUser.pop(deleteUserID.upper())
        deleteSuccessMsg()
        return True
    
    userNotFoundMsg()
    return False

# 7. Check Password Function

def checkPassword():
    while True:
        password1 = input("\nEnter a new password: ")
        password2 = input("Re-enter the new password: ")
        if password1 == password2:
            return password1
        else:
            passwordMismatchMsg()

# 8. Change Password Function

def changePassword(userID):
    if userID.upper() in appUser:
        while True:
            oldPassword = input("\nEnter your old password: ")
            if appUser[userID.upper()]["Password"] == oldPassword:
                newPassword = checkPassword()
                if userConfirmation() == True:
                    appUser[userID.upper()]["Password"] = newPassword
                    passwordChangeSuccessMsg()
                break
            else:
                passwordMismatchMsg()
    else:
        userNotFoundMsg()

# 9. Select Role Function

def selectRole():
    roleInput = input('''\nUser Roles:
1. Master Admin
2. Stock Manager
3. Kitchen Staff
Enter new user role [1/2/3]:''')
    if roleInput == "1":
        return "Master Admin"
    elif roleInput == "2":
        return "Stock Manager"
    elif roleInput == "3":
        return "Kitchen Staff"
    else:
        invalidInputMsg()
        selectRole()

# 10. Logout Function

def logout():
    if userConfirmation("Logout") == True:
        logoutSuccessMsg()
        module = importlib.import_module("main")
        module.main()
        return True
    return False