# stock.py details all stock-related data and functions

# --- IMPORTS --- #

import json
from datetime import datetime
from stock import checkStock, getCurrentStock, reduceStockExt
from messages import *

# --- DATA --- #

# Dictionary "restoMenu" defines the restaurant menu items and their ingredients

restoMenu = {
    "Fried Rice" : {
        "Egg" : 1,
        "Rice" : 2,
        "Sausage" : 1
    },
    "Soup" : {
        "Egg" : 1,
        "Carrot" : 2,
        "Sausage" : 1
    },
    "Corn Soup" : {
        "Carrot" : 1,
        "Corn" : 1
    },
    "Plain Rice" : {
        "Rice" : 1
    },
    "Sausage Barbeque" : {
        "Sausage" : 1,
        "Carrot" : 1
    },
    "Tea" : {
        "Tea" : 1
    }
}

# List of orders
orders = []


# --- FUNCTIONS --- #

# 1. Check menu existence function

def checkMenu(value=str):
    if value.lower().title() in restoMenu:
        return True
    else:
        return False
    
# 2. View menu items

def viewMenu():
    restoMenuMsg()
    index = 0
    for i in restoMenu:
        index += 1
        print(f"{index}. {i}")
    print("")
    
# 3. Place Order Function

def placeOrder(orderID=str, menuName=str, qty=int):
    menuName = menuName.lower().title()
    if menuName in restoMenu:
        if str(qty).isdigit() and int(qty) > 0:
            ingredients = getIngredients(menuName)

            for i in ingredients:
                if verifyStock(i, int(ingredients[i])*qty) == True:
                    continue
                else:
                    stockNotEnoughMsg()
                    break
            else:
                orders.append({
                    "Order ID" : orderID,
                    "Menu Item" : menuName,
                    "Quantity" : qty,
                    "Order Time" : datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                })

                for i in ingredients:
                    reduceStockExt(i, int(ingredients[i])*qty)

                orderSuccessMsg(" " + menuName)
                return True
        else:
            invalidQtyMsg()
            return False
    else:
        itemNotFoundMsg(menuName + " ")
        return False

# 4. Get Ingredients Function

def getIngredients(menuName=str):
    menuName = menuName.lower().title()
    if menuName in restoMenu:
        return dict(restoMenu[menuName].items())
    else:
        itemExistsMsg(menuName + " ")
        return None
    
# 5. Verify Stock Function

def verifyStock(ingredient=str, neededQty=int):
    ingredient = ingredient.lower().title()
    if str(neededQty).isdigit() and int(neededQty) > 0:
        if checkStock(ingredient) == True:
            currQty = getCurrentStock(ingredient)
            if int(currQty) >= int(neededQty):
                return True
            else:
                return False
        else:
            invalidIngredientMsg()
            return False
    else:
        invalidQtyMsg()
        return False

# 6. Update Stock Function

def updateStock(ingredient=str, stockUsed=int):
    ingredient = ingredient.lower().title()
    if str(stockUsed).isdigit() and int(stockUsed) > 0:
        if checkStock(ingredient) == True:
            reduceStockExt(ingredient, stockUsed)
        else:
            invalidIngredientMsg()
    else:
        invalidQtyMsg()
