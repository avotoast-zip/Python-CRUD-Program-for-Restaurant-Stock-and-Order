# stock.py details all stock-related data and functions

# --- IMPORTS --- #

import json
from datetime import datetime
from messages import *

# --- DATA --- #

# Dictionary "kitchenStock" defines the initial kitchen stock data

kitchenStock = {
    "Egg" : {
        "Quantity" : 20,
        "Last Update" : "2025-02-08 18:57:03"
    },
    "Rice" : {
        "Quantity" : 30,
        "Last Update" : "2025-02-08 18:57:03"
    },
    "Sausage" : {
        "Quantity" : 15,
        "Last Update" : "2025-02-08 18:57:03"
    },
    "Carrot" : {
        "Quantity" : 27,
        "Last Update" : "2025-02-08 18:57:03"
    },
    "Corn" : {
        "Quantity" : 15,
        "Last Update" : "2025-02-08 18:57:03"
    },
    "Tea" : {
        "Quantity" : 50,
        "Last Update" : "2025-02-08 18:57:03"
    }
}

# --- FUNCTIONS --- #

# 1. Check item existence function

def checkStock(value=str):
    if value.lower().title() in kitchenStock:
        return True
    else:
        return False
    
# 2. Get Stock Function

def getStock(itemName="All"):

    if (itemName.lower().title() in kitchenStock) or (itemName == "All"):

        if itemName == "All":
            print(json.dumps(kitchenStock, indent = 3))

        else:
            itemData = {key:value for key, value in kitchenStock[itemName.lower().title()].items()}
            print(f"Item Name: {itemName.lower().title()} {json.dumps(itemData, indent = 3)}")

    else:
        itemNotFoundMsg(str(itemName) + " ")

# 3. Modify Last Update Function

def updateTime(itemName=str):
    if itemName.lower().title() in kitchenStock:
        kitchenStock[itemName.lower().title()]["Last Update"] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

# 4. Add Stock Function

def addStock(itemName=str, addBy=int):
    itemName = itemName.lower().title()
    if itemName in kitchenStock:
        if str(addBy).isdigit() and int(addBy) > 0:
            if userConfirmation() == True:
                currentQty = kitchenStock[itemName]["Quantity"]
                kitchenStock[itemName]["Quantity"] = int(currentQty) + int(addBy)
                updateTime(itemName)
                updateSuccessMsg(itemName)
                currentStockMsg(getCurrentStock(itemName))
        else:
            invalidQtyMsg()
    else:
        itemNotFoundMsg(itemName + " ")

# 5. Reduce Stock Function

def reduceStock(itemName=str, reduceBy=int):
    itemName = itemName.lower().title()
    if itemName in kitchenStock:
        if str(reduceBy).isdigit() and int(reduceBy) > 0:
            if int(kitchenStock[itemName]["Quantity"]) >= int(reduceBy):
                if userConfirmation() == True:
                    currentQty = kitchenStock[itemName]["Quantity"]
                    kitchenStock[itemName]["Quantity"] = int(currentQty) - int(reduceBy)
                    updateTime(itemName)
                    updateSuccessMsg(itemName)
            else:
                stockNotEnoughMsg()
            currentStockMsg(getCurrentStock(itemName))
        else:
            invalidQtyMsg()
    else:
        itemNotFoundMsg(itemName + " ")

# 6. Add Item Function

def addItem(itemName=str, qty=int):
    itemName = itemName.lower().title()
    if itemName not in kitchenStock:
        if str(qty).isdigit() and int(qty) >= 0:
            kitchenStock[itemName] = {}
            kitchenStock[itemName]["Quantity"] = qty
            updateTime(itemName)
            addItemSuccessMsg()
            return True
        else:
            invalidQtyMsg()
            return False
    else:
        itemExistsMsg()
        return False
    
# 7. Get Current Stock Function
def getCurrentStock(itemName):
    itemName = itemName.lower().title()
    if itemName in kitchenStock:
        return kitchenStock[itemName]["Quantity"]
    else:
        itemNotFoundMsg(itemName + " ")
        return None
    
# 5. Reduce Stock External Function

def reduceStockExt(itemName=str, reduceBy=int):
    itemName = itemName.lower().title()
    if itemName in kitchenStock:
        if str(reduceBy).isdigit() and int(reduceBy) > 0:
            if int(kitchenStock[itemName]["Quantity"]) >= int(reduceBy):
                currentQty = kitchenStock[itemName]["Quantity"]
                kitchenStock[itemName]["Quantity"] = int(currentQty) - int(reduceBy)
                updateTime(itemName)
            else:
                stockNotEnoughMsg()
        else:
            invalidQtyMsg()
    else:
        itemNotFoundMsg(itemName + " ")
